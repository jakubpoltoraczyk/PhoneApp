from PyQt5.QtWidgets import QApplication, QDialog
import sys
from src.basis_app_class import PhoneApp
from src.my_entry import PhoneAppEntryBox


class Window(QDialog):
    # todo: in future to remove, now it is the first window of our application
    def __init__(self, master):
        super().__init__()
        self.master: PhoneApp = master
        self.entry1 = PhoneAppEntryBox(
            self,
            122,
            30,
            200,
            140,
            font_size=16,
            placeholder="jakies",
            type_name="hej ziom",
            text_changed_function=lambda: print("cos tam"),
        )


app = QApplication(sys.argv)
window = PhoneApp(app, "SPOTIFY", "style.css", Window, 1000, 800)
sys.exit(app.exec())
