import logging
import time

from utilities.logger.logger import Logger


class TestStep:
    logger = Logger.prepare_logger()

    @staticmethod
    def step(func):
        def print_step(self, *args, **kwargs):
            time_start = time.time()
            result = func(self, *args, **kwargs)
            time_end = time.time()
            method_name = func.__qualname__.replace("_", " ").replace(".", ": ")
            logging.getLogger("TEST_LOGGER").info(
                f"Step: {method_name} | time:{round((time_end - time_start) * 1000, 1)}ms")
            return func

        return print_step
