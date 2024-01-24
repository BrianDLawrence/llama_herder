import logging
import contextlib

logger = logging.getLogger("LLAMA_HERDER")

@contextlib.contextmanager
def error_handler(operation_description):
    try:
        yield
    except Exception as e:
        logger.exception(f"Error occurred during {operation_description}: {e}")
        # For now I will  re-raise the exception
        raise
