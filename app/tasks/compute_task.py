from app.utils.custom_dataframe import CustomDataFrame
from app.tasks.export_task import ExportTask
import pandas


class ComputeTask:
    """"""

    def __init__(self, ingestion_task_result: dict, export_task: ExportTask):
        self.ingestion_task_result = ingestion_task_result
        self.export_task = export_task

    def compute(self):
        """

        :return:
        """
        drugs = CustomDataFrame.create_df_from_file(self.ingestion_task_result.get("drugs"), "csv")
        clinical_trials = CustomDataFrame.create_df_from_file(self.ingestion_task_result.get("clinical_trials"), "csv")
        pubmed = CustomDataFrame.create_df_from_file(self.ingestion_task_result.get("pubmed"), "csv")

        pubmed['type'] = "pubmed"
        clinical_trials['type'] = "clinical_trials"
        pubmed_clinical_trials = pandas.concat([pubmed, clinical_trials])
        result = pandas.merge(pubmed_clinical_trials, drugs, how="cross")
        result = result[result.apply(lambda result_dataframe: result_dataframe.drug.upper() in result_dataframe.title.upper(), axis=1)]
        result = result[['drug', 'title', 'journal', 'date']]
        self.export_task.export(result)
