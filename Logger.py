import logging, logging.config
from FileLoader import FileLoader


class Logger:
	def __init__(self):
		self.fileLoader = FileLoader('Logger.json')
		self.logging_config =  self.fileLoader.loadFileData()
		logging.config.dictConfig(self.logging_config)
		self.logger = logging.getLogger(__name__)

	def debug(self, message):
		self.logger.debug(message)

	def info(self, message):
		self.logger.info(message)

	def warning(self, message):
		self.logger.warning(message)

	def error(self, message):
		self.logger.error(message)

	def critical(self, message):
		self.logger.critical(message)
		
