import krakenex
from datetime import datetime
from functools import wraps
from dataclasses import dataclass
import configparser
from influxdb import InfluxDBClient, DataFrameClient
import asyncio
from sample import sample_response


config = configparser.ConfigParser()
config.read('kraken.conf')

api = krakenex.API(key=config['default']['key'], secret=config['default']['secret'])


influx = InfluxDBClient(host=None, database=None)

call_counter = 0
max_calls = 15  # basic user account
last_call = None  #Time stamp of last api call


def rate_limiter(func):
    def wraps(last, counter, *args, **kwargs):

        return func


@dataclass()
class OpenPosition:
    """
    An object and methods for open positions
    """
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


req_data = {'docalcs': 'True'}


resp = api.query_private('OpenPositions', req_data)


positions = [OpenPosition(**v) for k, v in resp['result'].items()]

for position in positions:
    print(position)







