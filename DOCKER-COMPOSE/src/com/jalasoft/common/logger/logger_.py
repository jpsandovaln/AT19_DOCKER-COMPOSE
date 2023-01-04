#
# @logger_.py Copyright (c) 2022 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

from Singleton import SingletonMeta
import logging
import logging.config


class LoggerManager(metaclass=SingletonMeta):
    """Logger wrapper"""
    logging.config.fileConfig("logging.conf")

    def debug(self, message):
        """Write logger debug level"""
        logging.debug(message)
    
    def info(self, message):
        """Write logger info level"""
        logging.info(message)

    def warning(self, message):
        """Write logger warning level"""
        logging.warning(message)

    def error(self, message):
        """write logger error level"""
        logging.error(message)

    def critical(self, message):
        """Write logger critical level"""
        logging.critical(message)
