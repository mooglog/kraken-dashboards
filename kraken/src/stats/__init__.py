from influxdb import InfluxDBClient, SeriesHelper


influx = InfluxDBClient(
    host='localhost',
    port=8086,
    username='',
    password='',
    database='kraken')


class Stats(SeriesHelper):
    def __init__(self, series_name, tags, fields, **kw):
        self.series_name = series_name or kw['series_name']
        self.tags = tags or kw['tags']
        self.fields = fields or kw['fields']
        super().__init__(**kw)

    class Meta:
        series_name = ''
        tags = []
        fields = []
        client = influx

