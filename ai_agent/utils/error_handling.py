import logging
import contextlib

logger = logging.getLogger("LLAMA_HERDER")

@contextlib.contextmanager
def error_handler(operation_description):
    try:
        yield
    except Exception as e:
        logger.exception("Error occurred during %s with exception: %s",operation_description,e)
        raise
