import logging
import sys


class Logger:

    @staticmethod
    def prepare_logger():
        logger = logging.getLogger('TEST_LOGGER')
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter("%(asctime)s : %(message)s", datefmt="%d-%m-%Y %H:%M:%S")
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.propagate = False
        return logger
