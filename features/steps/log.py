import logging
import os

from pythonjsonlogger import jsonlogger


# Get custom logger
def get_custom_logger():
    log_path = "../../logs"
    file_name = "testSuite"
    logger = logging.getLogger(__name__)
    log_level = logging.DEBUG
    logger.setLevel(log_level)
    # log_formatter = logging.Formatter("%(asctime)s [%(name)-12.12s] [%(levelname)-5.5s] %(message)s")
    log_formatter = logging.Formatter("%(asctime)s\t %(levelname)-10.10s %(message)s")
    log_json_formatter = jsonlogger.JsonFormatter(fmt='%(asctime)s %(name)s %(levelname)s %(message)s')
    log_file_name = "{0}/{1}.log".format(log_path, file_name)
    os.makedirs(os.path.dirname(log_file_name), exist_ok=True)
    file_handler = logging.FileHandler(log_file_name)
    file_handler.setLevel(log_level)
    file_handler.setFormatter(log_json_formatter)
    logger.addHandler(file_handler)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_formatter)
    logger.addHandler(console_handler)
    return logger
