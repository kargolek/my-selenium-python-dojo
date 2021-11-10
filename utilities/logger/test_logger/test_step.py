import time
from typing import Callable
from functools import wraps
from typing import TypeVar, Any

from utilities.logger.logger import Logger

_TFunc = TypeVar("_TFunc", bound=Callable[..., Any])

logger = Logger.prepare_logger()


def test_step(arg):
    if callable(arg):
        return StepContext(arg.__name__, {})(arg)
    else:
        return StepContext(arg, {})


class StepContext:

    def __init__(self, arg, params):
        self.title = arg
        self.params = params

    def __call__(self, func: _TFunc) -> _TFunc:
        @wraps(func)
        def impl(*args, **kw):
            time_start = time.time()
            params = func(*args, **kw)
            time_end = time.time()
            method_name = func.__qualname__.replace("_", " ").replace(".", ": ")
            logger.info(f"Step: {method_name} | time:{round((time_end - time_start) * 1000, 1)}ms")
            return params

        return impl
