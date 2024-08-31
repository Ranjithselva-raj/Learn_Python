import logging

def module_b_function():
    logger = logging.getLogger(__name__)

    logger.info("module_b_function is called")
    logger.debug("this is a debug message from module_b")
    logger.info('Module B function finished')