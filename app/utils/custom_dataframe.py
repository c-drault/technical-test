import pandas
import os
from pandas import DataFrame
from app.utils.TTSException import TTSException
from app.utils.custom_logger import CustomLogger


class CustomDataFrame:
    logger = CustomLogger.get_logger("CustomDataFrame")

    @staticmethod
    def create_df_from_file(file_path: str, extension: str) -> DataFrame:
        """
        Create a pandas.DataFrame from a file.

        :param file_path: The complete file of the pass
        :param extension: Extension of the path
        :return: DataFrame
        """
        dataframe: DataFrame
        if extension == "csv":
            dataframe = pandas.read_csv(file_path)
        elif extension == "json":
            dataframe = pandas.read_json(file_path)
        else:
            raise TTSException(f"The extension [{extension}] is not recognise as a valid extension.")
        CustomDataFrame.logger.info(f"File [{file_path}] retrieve as dataframe")
        return dataframe

    @staticmethod
    def create_file_from_df(base_path: str, file_name: str, dataframe: DataFrame) -> str:
        """
        Create a file from a pandas.DataFrame.

        :param base_path: base path of the new file to create.
        :param file_name: complete name of the new file with extension.
        :param dataframe: dataframe we need to write.
        :return: The complete path of the new file created.
        """
        os.makedirs(base_path, exist_ok=True)
        path = base_path + file_name if base_path.endswith("/") else base_path + "/" + file_name
        if file_name.endswith(".csv"):
            dataframe.to_csv(path, index=False)
            CustomDataFrame.logger.info(f"File [{path}] created, in CSV")
        elif file_name.endswith(".json"):
            dataframe.to_json(path, orient="records")
            CustomDataFrame.logger.info(f"File [{path}] created, in JSON")
        else:
            raise TTSException(f"Extension is not recognise as a valid extension.")
        return path

    @staticmethod
    def convert_strcol_as_date(col, dataframe: DataFrame):
        dataframe[col["name"]] = pandas.to_datetime(dataframe[col["name"]], infer_datetime_format=True)
        return dataframe

    @staticmethod
    def rename_column(dataframe: DataFrame, col: dict) -> DataFrame:
        return dataframe.rename(columns={col["name"]: col["alias"]})