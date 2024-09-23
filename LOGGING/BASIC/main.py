import logging

# DEBUG: Detailed information, typically of interest only when diagnosing problems.

# INFO: Confirmation that things are working as expected.

# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

# ERROR: Due to a more serious problem, the software has not been able to perform some function.

# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

logging.basicConfig(
    filename="test.log", level=logging.DEBUG, format="%(asctime)s:%(name)s:%(message)s"
)


def add(a, b):
    return a + b


def minus(a, b):
    return a - b


def multipy(a, b):
    return a * b


def divide(a, b):
    return a / b


num_1 = 10
num_2 = 5

add_result = add(num_1, num_2)
logging.debug("ADD : {} + {} = {}".format(num_1, num_2, add_result))

sub_result = minus(num_1, num_2)
logging.debug("SUB : {} - {} = {}".format(num_1, num_2, sub_result))

mul_result = multipy(num_1, num_2)
logging.debug("MULTIPLICATION : {} * {} = {}".format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)
logging.debug("DIV : {} / {} = {}".format(num_1, num_2, div_result))
