
import json
import logging.config
from QtDesignerUI.QtLoggerConfigurationGeneratedGUI import *
from classes.Logger import LoggerConfigurationLoader

class LoggerWindow(QtWidgets.QDialog, Ui_QtLoggerConfigurationGenerated):
	def __init__(self, logger=None):
		super().__init__()
		self.logger = logger
		self.conf = LoggerConfigurationLoader()
		self.setupUi(self)
		self.loadConfigurtion()
	def loadConfigurtion(self):
		self.loggerPlainTextEdit.setPlainText(json.dumps(self.conf.load(), indent=4))
	def accept(self):
		config = self.loggerPlainTextEdit.toPlainText()
		self.conf.save(config)
		self.logger.logging_config = json.loads(config)
		logging.config.dictConfig(json.loads(config))
		super().accept()
