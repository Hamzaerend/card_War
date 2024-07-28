import random
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi("deste.ui",self)
        self.setWindowTitle("Oyna")

        self.kurpiyerlabel = self.findChild(QLabel, "kurpiyer_label")
        self.oyunculabel = self.findChild(QLabel, "oyuncu_label")
        self.kurpiyer_habel = self.findChild(QLabel, "klabel")
        self.oyuncu_hlabel = self.findChild(QLabel, "olabel")

        self.karistirbutton = self.findChild(QPushButton, "karistir_button")
        self.dagitbutton = self.findChild(QPushButton, "dagit_button")

        self.karistir()

        self.karistirbutton.clicked.connect(self.karistir)
        self.dagitbutton.clicked.connect(self.dagit)

        self.show()

    def karistir (self):
        suits = ["diamonds","clubs","hearts","spades"]
        values = range(2,15)

        global deste 
        deste = []

        for suit in suits:
            for value in values:
                deste.append(f"{value}_of_{suit}")

        global kurpiyer, oyuncu
        self.kurpiyer = []
        self.oyuncu = []
        self.kurpiyer_skor = 0
        self.oyuncu_skor = 0



        self.kurpiyer_kart = random.choice(deste) 
        deste.remove(self.kurpiyer_kart)
        self.kurpiyer.append(self.kurpiyer_kart)
        pixmap = QPixmap(f'C:/Users/hmzrndnc/pyqt5/cards/{self.kurpiyer_kart}.png')
        self.kurpiyerlabel.setPixmap(pixmap)

        self.oyuncu_kart = random.choice(deste) 
        deste.remove(self.oyuncu_kart)
        self.oyuncu.append(self.oyuncu_kart)
        pixmap = QPixmap(f'C:/Users/hmzrndnc/pyqt5/cards/{self.oyuncu_kart}.png')
        self.oyunculabel.setPixmap(pixmap)
        self.setWindowTitle(f" Destede {len(deste)} kart kaldı ")
        self.skor()

    def dagit (self):
        try:


            self.kurpiyer_kart = random.choice(deste) 
            deste.remove(self.kurpiyer_kart)
            self.kurpiyer.append(self.kurpiyer_kart)
            pixmap = QPixmap(f'C:/Users/hmzrndnc/pyqt5/cards/{self.kurpiyer_kart}.png')
            self.kurpiyerlabel.setPixmap(pixmap)

            self.oyuncu_kart = random.choice(deste) 
            deste.remove(self.oyuncu_kart)
            self.oyuncu.append(self.oyuncu_kart)
            pixmap = QPixmap(f'C:/Users/hmzrndnc/pyqt5/cards/{self.oyuncu_kart}.png')
            self.oyunculabel.setPixmap(pixmap)
            self.setWindowTitle(f" Destede {len(deste)} kart kaldı ")
            self.skor()
            
        except:
            if self.kurpiyer_skor == self.oyuncu_skor:
                self.setWindowTitle(f"Oyun Bitti || Eşitlik! || {self.kurpiyer_skor} to {self.oyuncu_skor}")
            elif self.kurpiyer_skor > self.oyuncu_skor:
                self.setWindowTitle(f"Oyun Bitti || Kurpiyer Kazandı! || {self.kurpiyer_skor} to {self.oyuncu_skor}")
            else:
                self.setWindowTitle(f"Oyun Bitti || Oyuncu Kazandı! || {self.kurpiyer_skor} to {self.oyuncu_skor}")

    def skor (self):
        self.kurpiyer_kart = int(self.kurpiyer_kart.split("_",1)[0])
        self.oyuncu_kart = int(self.oyuncu_kart.split("_",1)[0])

        if self.kurpiyer_kart == self.oyuncu_kart:
            self.kurpiyer_habel.setText("Eşitlik!")
            self.oyuncu_hlabel.setText("Eşitlik!")
            self.setWindowTitle(f" Destede {len(deste)} kart kaldı || Kurpiyer: {self.kurpiyer_skor} Oyuncu:{self.oyuncu_skor}")
        elif self.kurpiyer_kart > self.oyuncu_kart:
            self.kurpiyer_habel.setText("Kurpiyer Kazandı!")
            self.oyuncu_hlabel.setText("Oyuncu Kaybetti!")
            self.kurpiyer_skor = self.kurpiyer_skor+1
            self.setWindowTitle(f" Destede {len(deste)} kart kaldı || Kurpiyer: {self.kurpiyer_skor} Oyuncu:{self.oyuncu_skor}")
        else:
            self.kurpiyer_habel.setText("Kurpiyer Kaybetti!")
            self.oyuncu_hlabel.setText("Oyuncu Kazandı!")
            self.oyuncu_skor = self.oyuncu_skor+1
            self.setWindowTitle(f" Destede {len(deste)} kart kaldı || Kurpiyer: {self.kurpiyer_skor} Oyuncu:{self.oyuncu_skor}")
app= QApplication(sys.argv)
UIWindow = UI()
app.exec_()