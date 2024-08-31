from logger import logging

def add(a, b):
    try:
        result = a + b
        logging.debug(f"Adding {a} and {b}, {result}")
    except Exception as e:
        logging.error(e)
    else:
        logging.info(f"End of addition, returning result:{result}")
        return result

logging.debug("Addition function is called")
add(10,15)

def sub(a, b):
    try:
        result = a - b
        logging.debug(f"Subtracting {a} and {b}, {result}")
    except Exception as e:
        logging.error(e)
    else:
        logging.info(f"End of subtraction, returning result:{result}")
        return result

logging.debug("Subtraction function is called")
sub(10,15)

def div(a, b):
    try:
        result = a / b
        logging.debug(f"Division {a} and {b}, {result}")
    except Exception as e:
        logging.error(e)
    else:
        logging.info(f"End of Division, returning result:{result}")
        return result

logging.debug("Division function is called")
div(10,0)