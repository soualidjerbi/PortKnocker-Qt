import sys
from classes.Logger import Logger
from classes.Knocker import PortKnocker
from classes.Host import Host
from PyQt6.QtWidgets import (QTableWidgetItem, QComboBox)
from QtDesignerUI.QtPortKnockerGeneratedGUI import *
from QtLoggerWindow import LoggerWindow



class PortKnockerWindow(QtWidgets.QMainWindow, Ui_QtGeneratedMainWindow):
	def __init__(self):
		super().__init__()
		self.logger = Logger()
		self.knocker = PortKnocker(self.logger)
		self.confCatalogue, self.index = self.knocker.configurationLoader.load()
		self.setupUi(self)
		self.adjustTableFormat([self.openingGrid, self.closingGrid])
		self.setAdditionalComboParameters()
		self.setFields(self.confCatalogue[self.index])
	
	def byeBye(self):
		sys.exit()
	
	def addConfiguration(self):
		newConf = Host()
		self.confCatalogue.append(newConf)
		self.comboConfigurations.addItem('')
		self.index = len(self.confCatalogue) - 1
		self.comboConfigurations.setCurrentIndex(self.index)
		self.setFields(self.confCatalogue[self.index])

	def delConfiguration(self):
		index = self.comboConfigurations.currentIndex()
		self.index = index -1 if index >= len(self.confCatalogue) - 1 else index
		self.comboConfigurations.removeItem(index)
		self.confCatalogue.pop(index)
		self.comboConfigurations.setCurrentIndex(self.index)
		self.setFields(self.confCatalogue[self.index])

	def adjustTableFormat(self, grid):
		for i in range(grid.__len__()):
			grid[i].setHorizontalHeaderLabels(['Port', 'Protocol'])
			grid[i].setColumnWidth(0, 150)
			grid[i].setColumnWidth(1, 95)
			grid[i].verticalScrollBar().setEnabled(False)
			grid[i].horizontalScrollBar().setEnabled(False)
		
	def chkConnection(self):
		pass
	def openPorts(self):
		host = self.confCatalogue[self.index]
		self.knocker.configure(host)
		self.knocker.knock_in()
		
	def saveConfig(self ):
		self.logger.debug('------Save Config-------')
		self.knocker.configurationLoader.save(self.confCatalogue, self.index)
		
	def closePorts(self):
		host = self.confCatalogue[self.index]
		self.knocker.configure(host)
		self.knocker.knock_out()

	def setFields( self, configuration ):
		self.openingGrid = self.setGridValues(configuration.ports_in, self.openingGrid)
		self.closingGrid = self.setGridValues(configuration.ports_out, self.closingGrid)
		self.addressTxt.setText(configuration.ip_address)
		self.portTxt.setText(configuration.socket_port)
		
	def setGridValues(self, data, grid):
		for i, (port, protocol) in enumerate(data):
			grid.setItem(i, 0, QTableWidgetItem(port))
			grid.setItem(i, 1, QTableWidgetItem(protocol.upper()))
		return grid
	def getGridValuesAsList(self, grid):
		return [
			(grid.item(row, 0).text() if grid.item(row, 0) is not None else '',
			 grid.item(row, 1).text() if grid.item(row, 1) is not None else '')
			for row in range(grid.rowCount())
		]
	
	def setAdditionalComboParameters(self):
		self.comboConfigurations.setInsertPolicy(QComboBox.InsertPolicy.NoInsert)
		names = [conf.name for conf in self.confCatalogue]
		self.comboConfigurations.addItems(names)
		self.comboConfigurations.setCurrentIndex(self.index)
	
	def updateGridOn(self):
		self.confCatalogue[self.index].ports_in = self.getGridValuesAsList(self.openingGrid)

	def updateGridOff(self):
		self.confCatalogue[self.index].ports_out = self.getGridValuesAsList(self.closingGrid)

	def updateFields(self):
		self.logger.debug('------Update Fields------')
		self.index = self.comboConfigurations.currentIndex()
		self.logger.debug(f' self.index set to : {self.index}')
		self.setFields(self.confCatalogue[self.index])
		self.saveConfig()
		self.logger.debug('------Update Fields End--')
	def updateAddress(self):
		self.confCatalogue[self.index].ip_address = self.addressTxt.text()

	def updatePort(self):
		self.confCatalogue[self.index].socket_port = self.portTxt.text()
		
	def updateComboText(self):
		self.logger.debug('------Update Combo-------')
		self.index = self.comboConfigurations.currentIndex()
		comboText = self.comboConfigurations.currentText()
		self.confCatalogue[self.index].name = comboText
		self.comboConfigurations.setItemText(self.index, comboText)
		self.logger.debug('------Update Combo End---')
	def editLoggerConfig(self):
		logEditor = LoggerWindow(self.logger)
		logEditor.exec()