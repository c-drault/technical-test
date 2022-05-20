from app.tasks.ingestion_task import IngestionTask
from app.tasks.compute_task import ComputeTask
from app.tasks.export_task import ExportTask

import yaml
from app.utils.custom_logger import CustomLogger

if __name__ == '__main__':
    logger = CustomLogger.get_logger("Main")

    with open("./config/config.yml") as conf_file:
        conf = yaml.load(conf_file, Loader=yaml.FullLoader)

    logger.info("Launch ingestion task")
    ingestion_configuration = conf['ingestion']
    ingestion_task = IngestionTask(ingestion_configuration)
    ingestion_task_result = ingestion_task.run()

    logger.info("Configure export")
    export_configuration = conf["export"]
    export_task = ExportTask(export_configuration)

    logger.info("Launch compute task")
    compute_task = ComputeTask(ingestion_task_result, export_task )
    compute_task_result = compute_task.compute()
    logger.info("Tasks finished")

