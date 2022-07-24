from typing import Protocol, Dict, overload
from PyQt5.QtWidgets import QTabWidget, QWidget, QTabBar, QPushButton
from dataclasses import dataclass, field
from .basis_app_class import PhoneApp


@dataclass
class Tab:
    name: str
    master: type
    def __post_init__(self) -> None:
        self.tab_widget: QWidget = QWidget()
        but = QPushButton(self.tab_widget)
        but.clicked.connect(lambda : self.master.add_tab("jakis22", 2))



@dataclass
class TabWidget(QTabWidget):
    master: PhoneApp
    type_name: str = field(default="")

    def __post_init__(self) -> None:
        super().__init__()
        self.tabs: Dict[str, Tab] = {}
        if self.type_name:
            self.setObjectName(self.type_name)
        self.add_tab("first")
        self.add_tab("second")
        self.add_tab("third")
        self.add_tab("fourth")
        self.add_tab("5")
        self.add_tab("jakis", 2)
        self.__set_size()
    def __set_size(self):
        width = self.master.width
        width = int(width/len(self.tabs))
        if width>250:
            width=150
        self.setStyleSheet("QTabBar::tab{width: %spx}"%width)
        

    @overload
    def add_tab(self, name: str, index: int) -> None:
        ...

    @overload
    def add_tab(self, name: str) -> None:
        ...

    def add_tab(self, name: str, index: int = ...) -> None:
        print("xxx")
        if name not in self.tabs:
            tab = Tab(name, self)
            if isinstance(index, int):
                self.insertTab(index, tab.tab_widget, name)
            else:
                self.addTab(tab.tab_widget, name)
            self.tabs[name] = tab
            print
            self.__set_size()
        else:
            ...  # here should be something which inform programmist about the unintented behaviour of the program

    def remove_tab(self, name: str) -> None:
        if name in self.tabs:
            tab = self.tabs.pop(name)
            self.removeTab(self.indexOf(tab.tab_widget))

