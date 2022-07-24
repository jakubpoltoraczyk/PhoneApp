from PyQt5.QtWidgets import QApplication, QDialog, QLabel
import sys
from src.basis_app_class import PhoneApp
from src.tab_widget import TabWidget

class Window(QDialog):
    # todo: in future to remove, now it is the first window of our application
    def __init__(self, master):
        super().__init__()
        label = QLabel(self)
        label.setText("label1")


app = QApplication(sys.argv)
window = PhoneApp(app, "SPOTIFY", "style.css", TabWidget, 1000, 800)
sys.exit(app.exec())
