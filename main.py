import requests;
import time
import threading
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
        self.ui.labela.setText(ETH)
        self.ui.labelb.setText(SXP)


    def start(self):
        ETH="ETHUSDT"
        SXP="SXPUSDT"
        while (True):
            time.sleep(1)
            values = self.get_prices()
            self.ui.valuea.setText(values[ETH])
            self.ui.valueb.setText(values[SXP])
            self.ui.result.setText('eth/sxp: '+str(float(values[ETH])/float(values[SXP])))

    def set_values(self, values):
            ETH = "ETHUSDT"
            SXP = "SXPUSDT"
            self.ui.valuea.setText(values[ETH])
            self.ui.valueb.setText(values[SXP])
            print("hola")
            print((float(float(values[ETH])/float(values[SXP]))))
            self.ui.result.setText('eth/sxp: '+str(float(float(values[ETH])/float(values[SXP]))))

        
    def get_prices(self):
        eth = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT').json()
        sxp = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=SXPUSDT').json()
        print(eth)
        print(sxp)
        return {eth['symbol']:eth['price'],sxp['symbol']:sxp['price']}
        
app = QtWidgets.QApplication([])
application = mywindow()
application.show()
#thread
x = threading.Thread(target=application.start, args=())
x.start()
#end thread
sys.exit(app.exec())


print('finish')

