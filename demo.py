from us_visa.logger import logging

from us_visa.exception import USvisaException
import sys

#logging.info("Welcome to our custom logs")

try:
    a=10/"10"

except Exception as e:
    raise USvisaException(e,sys) from e