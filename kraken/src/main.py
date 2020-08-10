import krakenex
import configparser
from datetime import datetime
import json
from objects import OpenPosition
import asyncio
from dataclasses import asdict
from influxdb import InfluxDBClient
config = configparser.ConfigParser()
config.read('kraken.conf')

api = krakenex.API(key=config['default']['key'], secret=config['default']['secret'])

database = 'kraken'
influx = InfluxDBClient(
    host='localhost',
    port=8086,
    username='',
    password='',
    database=database
)

influx.create_database(database)
influx.create_retention_policy('90days_default', '90d', replication='1', database=database, default=True)


req_data = {'docalcs': 'True'}


async def get_open_positions():

    while True:
        resp = api.query_private('OpenPositions', req_data)
        positions = [OpenPosition(**v) for k, v in resp['result'].items()]
        for position in positions:
            fields = asdict(position)
            fields.pop('ordertxid')
            json_body = [
                {
                    "measurement": "kraken.stats.OpenPositions",
                    "tags": {
                        "ordertxid": position.ordertxid,
                        "pair": position.pair,
                        "posstatus": position.posstatus
                    },
                    "fields": fields
                }
            ]
            print(json_body)
            wrt = influx.write_points(json_body)
            print(f'wrote positions')
        await asyncio.sleep(60)


async def get_balance():

    while True:
        resp = api.query_private('Balance', req_data)
        print(f"Balance {resp.get('result')}")
        await asyncio.sleep(360)


async def get_trade_balance():

    while True:
        resp = api.query_private('TradeBalance')
        json_body = [
            {
                "measurement": "kraken.stats.TradeBalance",
                "fields": resp['result']
            }
        ]
        influx.write_points(json_body)
        print(f"Tradebal {resp.get('result')}")
        await asyncio.sleep(60)


loop = asyncio.get_event_loop()

if __name__ == "__main__":
    asyncio.ensure_future(get_open_positions())
    # asyncio.ensure_future(get_balance())
    asyncio.ensure_future(get_trade_balance())
    loop.run_forever()




