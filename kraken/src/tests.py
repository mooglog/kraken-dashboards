import unittest
from .stats import Stats


class MyTestCase(unittest.TestCase):

    def _series_helper(self):
        stat = Stats(
            series_name='test',
            tags=['tag1', 'tag2'],
            fields=['field', 'field1', 'field2']
        )
        self.assertEqual(stat, stat)




if __name__ == '__main__':
    unittest.main()


