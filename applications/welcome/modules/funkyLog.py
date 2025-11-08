import logging
import os
from gluon import current
def get_logger():
    logger = logging.getLogger("web2py.app.welcome")
    log_file_path = os.path.join(current.request.folder, 'logs', 'welcome.log')
    file_handler = logging.FileHandler(log_file_path)
    logger.addHandler(file_handler)
    return logger