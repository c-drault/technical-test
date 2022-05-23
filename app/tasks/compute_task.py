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

        pubmed_drug = pandas.merge(drugs, pubmed, how="cross")
        pubmed_drug = pubmed_drug[pubmed_drug.apply(
            lambda pubmed_drug_e: pubmed_drug_e.drug.upper() in pubmed_drug_e.title.upper(), axis=1)]
        pubmed_drug = (pubmed_drug.groupby(['drug'])
                       .apply(lambda x: x[['title', 'journal', "date"]].to_dict('records'))
                       .reset_index()
                       .rename(columns={0: 'pubmed'})
                       )

        clinical_trials_drug = pandas.merge(drugs, clinical_trials, how="cross")
        clinical_trials_drug = clinical_trials_drug[clinical_trials_drug.apply(
            lambda clinical_trials_drug_e: clinical_trials_drug_e.drug.upper() in clinical_trials_drug_e.title.upper(), axis=1)]
        clinical_trials_drug = (clinical_trials_drug.groupby(['drug'])
                                .apply(lambda x: x[['title', 'journal', "date"]].to_dict('records'))
                                .reset_index()
                                .rename(columns={0: 'clinical_trials'})
                                )

        result = pandas.merge(clinical_trials_drug, pubmed_drug, on="drug", how="right")
        self.export_task.export(result)
