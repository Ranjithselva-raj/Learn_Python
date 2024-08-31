import logging

def module_a_function():
    logger = logging.getLogger(__name__)

    logger.info("module_a_function is called")
    logger.debug("this is a debug message from module_a")
    logger.info('Module A function finished')