from PyQt5.QtWidgets import QApplication, QDialog
import sys
from src.my_entry import MyEntry
from src.phone_app import PhoneApp


class Window(QDialog):
    # todo: in future to remove, now it is the first window of our application
    def __init__(self, master):
        super().__init__()
        self.master: PhoneApp = master
        self.entry1 = MyEntry(self, placeholder="cos")


app = QApplication(sys.argv)
window = PhoneApp(app, "SPOTIFY", "style.css", Window, 1000, 800)
sys.exit(app.exec())
