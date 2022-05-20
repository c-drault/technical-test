import logging


class CustomLogger:
    """
    Custom logger class for the project.
    """
    @staticmethod
    def get_logger(txt: str):
        FORMAT = '%(asctime)s [%(name)s]-%(levelname)s : %(message)s'
        logging.basicConfig(format=FORMAT, level=logging.DEBUG)
        logger = logging.getLogger("" + txt)
        return logger