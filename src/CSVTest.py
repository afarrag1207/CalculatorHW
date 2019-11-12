import unittest
from CSVReader import CSVReader, ClassFactory

class MyTestCase(unittest.TestCase):

  def setUp(self) -> None:
      self.csv_reader = CsvReader('Tests/Data/employee_birthday.csv')

  def test_return_data_as_objects(self):
      people = self.csv_reader.return_data_as_object


if __name__ == '__main__':
    unittest.main()
