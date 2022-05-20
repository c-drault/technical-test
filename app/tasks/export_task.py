from pandas import DataFrame
from app.utils.custom_dataframe import CustomDataFrame
from app.utils.custom_logger import CustomLogger


class ExportTask:
    """"""

    def __init__(self, config: dict):
        self.config = config

    def export(self, dataframe: DataFrame):
        """

        :return:
        """
        logger = CustomLogger.get_logger(ExportTask.__name__)
        CustomDataFrame.create_file_from_df(self.config["path"], self.config["name"] + "." + self.config["extension"], dataframe)


