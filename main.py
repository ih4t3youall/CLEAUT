import requests;
import sys
from PyQt5 import QtWidgets,QtGui
from ui.cleautui import Ui_MainWindow  # importing our generated file
from PyQt5.QtWidgets import (QApplication, QWidget, QMessageBox)
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg

class mywindow(QtWidgets.QMainWindow):


    def __init__(self):
        super(mywindow, self).__init__()
        ETH="ETHUSDT"
        SXP="SXPUSDT"
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        values = self.get_prices()
        self.ui.labela.setText('ETHUSDT')
        self.ui.labelb.setText('SXPUSDT')
        self.ui.valuea.setText(values[ETH])
        self.ui.valueb.setText(values[SXP])

        
    def get_prices(self):
        eth = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT').json()
        sxp = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=SXPUSDT').json()
        print(eth)
        print(sxp)
        return {eth['symbol']:eth['price'],sxp['symbol']:sxp['price']}
        
app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())
