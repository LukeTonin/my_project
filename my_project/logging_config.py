import inspect
import sys
import logging
import logging.handlers
from os.path import join, dirname

from . import ROOT_DIR

class ModifyModuleName(logging.Filter):
    def filter(self, record):
        record.name = simplify_logger_name(record.name)
        return True

def simplify_logger_name(logger_name: str):
    """Simple function to reduce the size of the loggers name.

    Parameters:
        logger_name (str): Name of the logger to simplify.
            e.g path.to.my_module
    
    Examples:
        simplify_logger_name('path.to.my_module') = 'p.t.mm'
    """
    modules = [module.split('_') for module in logger_name.split('.')]

    simplified = '.'.join([''.join(element[0] for element in elements) for elements in modules])
    
    return simplified

def configure_logger():
    """Function to configure the logger.
    """
        
    package_name = inspect.getmodule(inspect.stack()[1][0]).__name__
    logger = logging.getLogger(package_name)
    logger.propagate = False

    for handler in logger.handlers:
        logger.removeHandler(handler)

    handler = logging.StreamHandler(sys.stdout)
    handler.addFilter(ModifyModuleName())
    formatter = logging.Formatter('%(asctime)s - %(name)s:%(lineno)s - %(levelname)s - %(message)s', '%Y-%m-%d %H:%M:%S')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Add rotating file debug handler.
    rotating_file_handler = logging.handlers.RotatingFileHandler(
        join(dirname(ROOT_DIR), 'log.txt'), maxBytes=1000000, backupCount=0)
    rotating_file_handler.setLevel(logging.DEBUG)
    rotating_file_handler.setFormatter(formatter)
    logger.addHandler(rotating_file_handler)