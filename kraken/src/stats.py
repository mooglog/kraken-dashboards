from influxdb import InfluxDBClient, DataFrameClient, SeriesHelper


influx = InfluxDBClient(
    host='localhost',
    port=8086,
    username='',
    password='',
    database='kraken')


class Stats(SeriesHelper):
    def __init__(self, **kw):
        self.series_name = kw['series_name']
        self.tags = kw['tags']
        self.fields = kw['fields']


        super().__init__(**kw)

    class Meta:
        series_name =
        tags = []
        fields = []
        client = influx




