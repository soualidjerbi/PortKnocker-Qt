import logging, logging.config
from classes.FileLoader import FileLoader
from dataclasses import dataclass, field

@dataclass
class LoggerConfigurationLoader():
	fileLoader : dict = None
	loggerConfigFileName : str = field(default='Logger.json')
	
	def load(self) -> dict:
		return FileLoader().loadFileData(self.loggerConfigFileName)

	def save(self,config) -> None:
		FileLoader().saveTextToFile(self.loggerConfigFileName, config)

class Logger:
	def __init__(self):
		logging_config = LoggerConfigurationLoader().load()
		logging.config.dictConfig(logging_config)
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