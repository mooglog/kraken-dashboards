import krakenex
import datetime

import configparser
import json
from influxdb import InfluxDBClient, DataFrameClient

influx = InfluxDBClient(
    host=None,
    database=None
)


config = configparser.ConfigParser()
config.read('kraken.conf')

api = krakenex.API(key=config['default']['key'], secret=config['default']['secret'])


class CallRateHandler:

    def __init__(self, api, tier='Intermediate', retry=1, crl_sleep=5):

        self.api = api

        # api call rate limiter
        self.time_of_last_public_query = datetime.datetime.now()
        self.time_of_last_query = datetime.datetime.now()

        self.api_counter = 0

        if tier == 'None':
            self.limit = float('inf')
            self.factor = 3  # does not matter

        elif tier == 'Starter':
            self.limit = 15
            self.factor = 3  # down by 1 every three seconds

        elif tier == 'Intermediate':
            self.limit = 20
            self.factor = 2  # down by 1 every two seconds

        elif tier == 'Pro':
            self.limit = 20
            self.factor = 1  # down by 1 every one second

        # retry timers
        self.retry = retry
        self.crl_sleep = crl_sleep


    def request(api, method, **kwargs):
        data = {arg: value for arg, value in locals().items() if
                arg != 'self' and value is not None}

        # query

        res = api.query_private(method, data=data)

        # check for error
        try:
            assert len(res['error']) == 0

            print(res['results'])
            return res['results']


        except AssertionError:
            print(res['error'])





class Base(object):

    def __init__(self, **kwargs):
        for field in self.__annotations__:
            if field in kwargs:
                setattr(self, field, kwargs.get(field))
            else:
                setattr(self, field, None)

    def __repr__(self):
        return self.__class__.__name__


class OpenPosition(Base):
    ordertxid: str
    posstatus: str
    pair: str
    time: datetime
    type: str
    ordertype: str
    cost: float
    fee: float
    vol: float
    vol_closed: float
    margin: float
    value: float
    net: float
    terms: str
    rollovertm: datetime
    misc: str
    oflags: str

    def __init__(self):
        super().__init__()

    def __str__(self):
        for key, value in self.__dict__.items():
            return f'{key}: {value}'


openspos = generate(api, method='OpenPositions', docalcs=False)

