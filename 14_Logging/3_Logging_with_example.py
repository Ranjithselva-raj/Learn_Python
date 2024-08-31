import logging

#logging configuration

logging.basicConfig(
    level=logging.DEBUG,
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p',
    handlers= [
        logging.FileHandler('app1.log'),
        logging.StreamHandler()
    ]   
)

logger = logging.getLogger("ArithmeticCalculations")

def add(a, b):
    try:
        result = a + b
        logger.debug(f"Adding {a} + {b}, {result}")
    except Exception as e:
        logger.error(e)
    else:
        logger.info(f"End of addition, returning result:{result}")
        return result
    

def subtract(a, b):
    try:
        result = a - b
        logger.debug(f"subtract {a} - {b}, {result}")
    except Exception as e:
        logger.error(e)
    else:
        logger.info(f"End of subtract, returning result:{result}")
        return result
    
def multiply(a, b):
    try:
        result = a * b
        logger.debug(f"multiply {a} * {b}, {result}")
    except Exception as e:
        logger.error(e)
        return None
    else:
        logger.info(f"End of multiply, returning result:{result}")
        return result
    
def divide(a, b):
    try:
        result = a / b
        logger.debug(f"divide {a} / {b}, {result}")
    except Exception as e:
        logger.error(e)
    else:
        logger.info(f"End of divide, returning result:{result}")
        return result
logger.debug("Addition function is called")
add(10,15)
logger.debug("Subtraction function is called")
subtract(10,15)
logger.debug("Multiplication function is called")
multiply(10,15)
logger.debug("Division function is called")
divide(10,2)