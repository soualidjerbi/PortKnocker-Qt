import sys
from PyQt6 import QtWidgets
from QtPortKnockerWindow import PortKnockerWindow


class QtMain:
    def __init__(self):
        pass

    def main(self):
        app = QtWidgets.QApplication(sys.argv)
        mainwin = PortKnockerWindow()
        mainwin.show()
        app.exec()
    
if __name__ == '__main__':
    app = QtMain()
    app.main()