import unittest
from CSVReader  import CsvReader, ClassFactory


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.csv_reader = CsvReader('UnitTestAddition.csv')

    def test_return_data_as_objects(self):
        Value1 = self.csv_reader.return_data_as_objects('Value1')
        Value2 = self.csv_reader.return_data_as_objects('Value2')
        Result = self.csv_reader.return_data_as_objects('Result')
        self.assertIsInstance(Value1, Value2, Result, list)
        test_class = ClassFactory('Value1', self.csv_reader.data[0])
        for Value1 in Result:
            self.assertEqual(Value1.__name__, test_class.__name__)


if __name__ == '__main__':
    unittest.main()