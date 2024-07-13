# Form implementation generated from reading ui file 'QtPortKnockerGeneratedGUI.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_QtGeneratedMainWindow(object):
    def setupUi(self, QtGeneratedMainWindow):
        QtGeneratedMainWindow.setObjectName("QtGeneratedMainWindow")
        QtGeneratedMainWindow.resize(571, 309)
        self.centralwidget = QtWidgets.QWidget(parent=QtGeneratedMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.openingGrid = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.openingGrid.setGeometry(QtCore.QRect(10, 80, 271, 151))
        self.openingGrid.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.openingGrid.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.openingGrid.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.openingGrid.setShowGrid(False)
        self.openingGrid.setRowCount(4)
        self.openingGrid.setColumnCount(2)
        self.openingGrid.setObjectName("openingGrid")
        self.comboConfigurations = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboConfigurations.setGeometry(QtCore.QRect(10, 10, 271, 26))
        self.comboConfigurations.setEditable(True)
        self.comboConfigurations.setObjectName("comboConfigurations")
        self.closingGrid = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.closingGrid.setGeometry(QtCore.QRect(290, 80, 271, 151))
        self.closingGrid.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.closingGrid.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.closingGrid.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.closingGrid.setShowGrid(False)
        self.closingGrid.setRowCount(4)
        self.closingGrid.setColumnCount(2)
        self.closingGrid.setObjectName("closingGrid")
        self.closingGrid.horizontalHeader().setVisible(True)
        self.addressTxt = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.addressTxt.setGeometry(QtCore.QRect(290, 10, 191, 21))
        self.addressTxt.setObjectName("addressTxt")
        self.portTxt = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.portTxt.setGeometry(QtCore.QRect(490, 10, 71, 21))
        self.portTxt.setObjectName("portTxt")
        self.closeAppBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.closeAppBtn.setGeometry(QtCore.QRect(430, 240, 113, 32))
        self.closeAppBtn.setObjectName("closeAppBtn")
        self.closePortsBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.closePortsBtn.setGeometry(QtCore.QRect(310, 240, 113, 32))
        self.closePortsBtn.setObjectName("closePortsBtn")
        self.openPortsBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.openPortsBtn.setGeometry(QtCore.QRect(150, 240, 113, 32))
        self.openPortsBtn.setObjectName("openPortsBtn")
        self.delConfBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.delConfBtn.setGeometry(QtCore.QRect(152, 40, 131, 32))
        self.delConfBtn.setObjectName("delConfBtn")
        self.addConfBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.addConfBtn.setGeometry(QtCore.QRect(10, 40, 131, 32))
        self.addConfBtn.setObjectName("addConfBtn")
        self.saveBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.saveBtn.setGeometry(QtCore.QRect(30, 240, 113, 32))
        self.saveBtn.setObjectName("saveBtn")
        QtGeneratedMainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(parent=QtGeneratedMainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 571, 24))
        self.menuBar.setObjectName("menuBar")
        self.menuFichier = QtWidgets.QMenu(parent=self.menuBar)
        self.menuFichier.setObjectName("menuFichier")
        self.menuConfiguration = QtWidgets.QMenu(parent=self.menuBar)
        self.menuConfiguration.setObjectName("menuConfiguration")
        QtGeneratedMainWindow.setMenuBar(self.menuBar)
        self.actionEditConfiguration = QtGui.QAction(parent=QtGeneratedMainWindow)
        self.actionEditConfiguration.setObjectName("actionEditConfiguration")
        self.actionSave = QtGui.QAction(parent=QtGeneratedMainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionQuit = QtGui.QAction(parent=QtGeneratedMainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFichier.addAction(self.actionSave)
        self.menuConfiguration.addAction(self.actionEditConfiguration)
        self.menuBar.addAction(self.menuFichier.menuAction())
        self.menuBar.addAction(self.menuConfiguration.menuAction())

        self.retranslateUi(QtGeneratedMainWindow)
        self.closeAppBtn.clicked.connect(QtGeneratedMainWindow.byeBye) # type: ignore
        self.closePortsBtn.clicked.connect(QtGeneratedMainWindow.closePorts) # type: ignore
        self.openPortsBtn.clicked.connect(QtGeneratedMainWindow.openPorts) # type: ignore
        self.openingGrid.cellChanged['int','int'].connect(QtGeneratedMainWindow.updateGridOn) # type: ignore
        self.closingGrid.cellChanged['int','int'].connect(QtGeneratedMainWindow.updateGridOff) # type: ignore
        self.comboConfigurations.currentIndexChanged['int'].connect(QtGeneratedMainWindow.updateFields) # type: ignore
        self.comboConfigurations.currentTextChanged['QString'].connect(QtGeneratedMainWindow.updateComboText) # type: ignore
        self.saveBtn.clicked.connect(QtGeneratedMainWindow.saveConfig) # type: ignore
        self.addConfBtn.clicked.connect(QtGeneratedMainWindow.addConfiguration) # type: ignore
        self.delConfBtn.clicked.connect(QtGeneratedMainWindow.delConfiguration) # type: ignore
        self.addressTxt.textChanged['QString'].connect(QtGeneratedMainWindow.updateAddress) # type: ignore
        self.portTxt.textChanged['QString'].connect(QtGeneratedMainWindow.updatePort) # type: ignore
        self.actionSave.triggered.connect(QtGeneratedMainWindow.saveConfig) # type: ignore
        self.actionEditConfiguration.triggered.connect(QtGeneratedMainWindow.editLoggerConfig) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(QtGeneratedMainWindow)
        QtGeneratedMainWindow.setTabOrder(self.comboConfigurations, self.addressTxt)
        QtGeneratedMainWindow.setTabOrder(self.addressTxt, self.portTxt)
        QtGeneratedMainWindow.setTabOrder(self.portTxt, self.addConfBtn)
        QtGeneratedMainWindow.setTabOrder(self.addConfBtn, self.delConfBtn)
        QtGeneratedMainWindow.setTabOrder(self.delConfBtn, self.openingGrid)
        QtGeneratedMainWindow.setTabOrder(self.openingGrid, self.closingGrid)
        QtGeneratedMainWindow.setTabOrder(self.closingGrid, self.openPortsBtn)
        QtGeneratedMainWindow.setTabOrder(self.openPortsBtn, self.closePortsBtn)
        QtGeneratedMainWindow.setTabOrder(self.closePortsBtn, self.closeAppBtn)

    def retranslateUi(self, QtGeneratedMainWindow):
        _translate = QtCore.QCoreApplication.translate
        QtGeneratedMainWindow.setWindowTitle(_translate("QtGeneratedMainWindow", "Port Knocker"))
        self.closeAppBtn.setText(_translate("QtGeneratedMainWindow", "Close"))
        self.closePortsBtn.setText(_translate("QtGeneratedMainWindow", "Knock Out"))
        self.openPortsBtn.setText(_translate("QtGeneratedMainWindow", "Knock In"))
        self.delConfBtn.setText(_translate("QtGeneratedMainWindow", "Delete Conf"))
        self.addConfBtn.setText(_translate("QtGeneratedMainWindow", "Add Conf"))
        self.saveBtn.setText(_translate("QtGeneratedMainWindow", "Save"))
        self.menuFichier.setTitle(_translate("QtGeneratedMainWindow", "File"))
        self.menuConfiguration.setTitle(_translate("QtGeneratedMainWindow", "Configuration"))
        self.actionEditConfiguration.setText(_translate("QtGeneratedMainWindow", "Edit Configuration"))
        self.actionSave.setText(_translate("QtGeneratedMainWindow", "Save"))
        self.actionQuit.setText(_translate("QtGeneratedMainWindow", "Quit"))
