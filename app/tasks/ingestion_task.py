from app.tasks.normalisation_task import NormalisationTask
from app.utils.custom_dataframe import CustomDataFrame
from pandas import DataFrame
import pandas


class IngestionTask:
    """
    Task uses to ingest data.
    """

    def __init__(self, conf):
        self.conf = conf

    def run(self) -> dict:
        """
        Main method of this task, use to launch the ingestion.
        :return: Dict of file ingested with them localisation
        """
        response = {}
        for data in self.conf['data']:
            response[data["name"]] = self.individual_run(data)
        return response

    def individual_run(self, data: dict):
        """
        Method to launch one by one the ingestion on data.
        :param data: The information about the data we are going to ingest.
        :return: The path where the data is write after ingestion and normalisation.
        """
        dataframe: DataFrame = self.create_dataframe(data["files"])
        normalisation_task = NormalisationTask()
        before_compute_dataframe = normalisation_task.run(dataframe, data)
        path = CustomDataFrame.create_file_from_df(
            self.conf["output-folder"], data["name"] + ".csv", before_compute_dataframe)
        return path

    def create_dataframe(self, files: dict):
        """
        Usefull method to create a dataframe from one or multiple file
        :param files: the list of file we have to concider
        :return: The dataframe feed with file(s)
        """
        dfs: [DataFrame] = []
        for file in files:
            tmp_df: DataFrame = CustomDataFrame.create_df_from_file(self.conf["data-location"] + file["file-name"], file["extension"])
            dfs.append(tmp_df)
        dataframe: DataFrame = pandas.concat(dfs, ignore_index=True)
        return dataframe
