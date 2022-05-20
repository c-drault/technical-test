import pandas
from pandas import DataFrame
from app.utils.custom_dataframe import CustomDataFrame


class NormalisationTask:
    """"""

    def run(self, dataframe: DataFrame, data: dict) -> DataFrame:
        """

        :return:
        """
        for col in data["cols"]:
            if "alias" in col:
                dataframe = CustomDataFrame.rename_column(dataframe, col)
            if col["type"] == "date":
                dataframe = CustomDataFrame.convert_strcol_as_date(col, dataframe)
        return dataframe
