sample_response = {
  'error': [],
  'result': {
    'TS2NFH-6G7AX-7Mnnnn': {
      'ordertxid': 'OOCFUW-GLE3C-GExxxx',
      'posstatus': 'open',
      'pair': 'DASHXBT',
      'time': 1592949178.8092,
      'type': 'buy',
      'ordertype': 'market',
      'cost': '0.00859219',
      'fee': '0.00002406',
      'vol': '1.11297800',
      'vol_closed': '0.00000000',
      'margin': '0.00286406',
      'value': '0.00854',
      'net': '-0.0000500800',
      'terms': '0.0200% per 4 hours',
      'rollovertm': '1593150961',
      'misc': '',
      'oflags': ''
    },
    'TFIXSF-JNMBK-QGnnnn': {
      'ordertxid': 'OEUDDE-MJA75-KKxxxx',
      'posstatus': 'open',
      'pair': 'ADAXBT',
      'time': 1592965675.8291,
      'type': 'sell',
      'ordertype': 'market',
      'cost': '0.004410000',
      'fee': '0.000012348',
      'vol': '500.00000000',
      'vol_closed': '0.00000000',
      'margin': '0.001470000',
      'value': '0.00436750',
      'net': '+0.0000425000',
      'terms': '0.0200% per 4 hours',
      'rollovertm': '1593153019',
      'misc': '',
      'oflags': ''
    },
    'TWVKEJ-4T4M7-VNnnnn': {
      'ordertxid': 'OX5ELS-OZQHJ-OFxxxx',
      'posstatus': 'open',
      'pair': 'XXBTZUSD',
      'time': 1593016494.3508,
      'type': 'sell',
      'ordertype': 'market',
      'cost': '90.16145',
      'fee': '0.24344',
      'vol': '0.00971892',
      'vol_closed': '0.00000000',
      'margin': '30.05382',
      'value': '89.6',
      'net': '+0.5039',
      'terms': '0.0100% per 4 hours',
      'rollovertm': '1593146243',
      'misc': '',
      'oflags': ''
    },
    'TNEFQZ-HJHOR-DQnnnn': {
      'ordertxid': 'OAKWS5-TTPLU-J3xxxx',
      'posstatus': 'open',
      'pair': 'XXBTZUSD',
      'time': 1593083227.8545,
      'type': 'sell',
      'ordertype': 'market',
      'cost': '419.99549',
      'fee': '1.13399',
      'vol': '0.04540639',
      'vol_closed': '0.00000000',
      'margin': '83.99910',
      'value': '418.8',
      'net': '+1.1192',
      'terms': '0.0100% per 4 hours',
      'rollovertm': '1593155317',
      'misc': '',
      'oflags': ''
    }
  }
}

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