from abc import ABC, abstractproperty
from dataclasses import dataclass
from typing import Protocol
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QPushButton
import sys
from src.basis_app_class import PhoneApp
from src.my_entry import PhoneAppEntryBox


class Window(QDialog):
    # todo: in future to remove, now it is the first window of our application
    def __init__(self, master):
        super().__init__()
        self.master : PhoneApp = master
        self.entry1 = PhoneAppEntryBox(self, 122, 30, 200, 140, 16, "jakies", "hej ziom", text_changed_function=lambda : print("cos tam"))
        but = QPushButton(self)
        but.setGeometry(400, 140,20, 20)
        but.clicked.connect(lambda : self.entry1.set_font(7))
        self.entry2 = PhoneAppEntryBox(self, 122, 30, 200, 240, 16, "jakies", "hej ziom", text_changed_function=lambda : print("cos tam"))
        but = QPushButton(self)
        but.setGeometry(400, 240,20, 20)
        but.clicked.connect(lambda : self.entry2.set_font(7))
        self.entry3 = PhoneAppEntryBox(self, 122, 30, 200, 340, 16, "jakies", "hej ziom", text_changed_function=lambda : print("cos tam"))
        but = QPushButton(self)
        but.setGeometry(400, 340,20, 20)
        but.clicked.connect(lambda : self.entry3.set_font(7))
        self.entry4 = PhoneAppEntryBox(self, 122, 30, 200, 440, 16, "jakies", "hej ziom", text_changed_function=lambda : print("cos tam"))
        but = QPushButton(self)
        but.setGeometry(400, 440,20, 20)
        but.clicked.connect(lambda : self.entry4.set_font(7))


app = QApplication(sys.argv)
window = PhoneApp(app, "SPOTIFY", "style.css", Window, 1000, 800)
sys.exit(app.exec())