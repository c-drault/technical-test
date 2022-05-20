import unittest

import pandas
from pandas import DataFrame
from app.utils.custom_dataframe import CustomDataFrame
from app.utils.TTSException import TTSException


class TestCustomDataFrame(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_create_dataframe_from_json_file(self) -> None:
        df: DataFrame = CustomDataFrame.create_df_from_file("../resources/pubmed.csv", "csv")
        self.assertEqual(df.size, 8)

    def test_create_dataframe_from_csv_file(self) -> None:
        df: DataFrame = CustomDataFrame.create_df_from_file("../resources/pubmed.json", "json")
        self.assertEqual(df.size, 8)

    def test_create_dataframe_from_file_should_generate_exception_cause_extension_unknow(self):
        with self.assertRaises(TTSException):
            CustomDataFrame.create_df_from_file("../resources/pubmed.parquet", "parquet")

    def test_create_dataframe_from_no_file_should_generate_exception_cause_file_unknow(self):
        with self.assertRaises(Exception):
            CustomDataFrame.create_df_from_file("../../resources/untest.json", "json")

    def test_create_dataframe_from_file_should_generate_exception_cause_extension_dont_match_file(self):
        with self.assertRaises(Exception):
            CustomDataFrame.create_df_from_file("../resources/pubmed.json", "csv")

    # create_file_from_df
    def test_create_csv_file_from_dataframe(self):
        df: DataFrame = pandas.read_csv("../resources/pubmed.csv")
        pass

    def test_create_json_file_from_dataframe(self):
        pass

    def test_create_json_file_from_dataframe_when_file_already_exists(self):
        pass

    def test_create_json_file_from_dataframe_when_folder_dont_exists(self):
        pass