import krakenex
from pykrakenapi import KrakenAPI
import configparser
import json
from influxdb import InfluxDBClient, DataFrameClient

influx = InfluxDBClient(
    host=None,
    database=None
)

influxdf = DataFrameClient(
    host=None,
    database=None
)


def write_points(type, df):
    if type == df:
        influxdf.write_points(df)
    influx.wr


config = configparser.ConfigParser()
config.read('kraken.conf')

api = krakenex.API(key=config['default']['key'], secret=config['default']['secret'])
k = KrakenAPI(api)

x = k.get_trade_balance(asset='USD')

print(x)
