
import json
import logging.config
from classes.FileLoader import FileLoader
from QtDesignerUI.QtLoggerConfigurationGeneratedGUI import *

class LoggerWindow(QtWidgets.QDialog, Ui_QtLoggerConfigurationGenerated):
	def __init__(self, logger=None):
		super().__init__()
		self.logger = logger
		self.setupUi(self)
		self.loadConfigurtion()
	def loadConfigurtion(self):
		self.loggerPlainTextEdit.setPlainText(json.dumps(self.logger.logging_config, indent=4))
	def accept(self):
		config = self.loggerPlainTextEdit.toPlainText()
		self.logger.fileLoader.saveTextToFile(config)
		self.logger.logging_config = json.loads(config)
		logging.config.dictConfig(json.loads(config))
		super().accept()
