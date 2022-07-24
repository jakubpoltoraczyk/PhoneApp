from dataclasses import dataclass, field
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtGui import QFont
from typing import Callable
from .base_widget import BaseWidget

@dataclass
class PhoneAppEntryBox(BaseWidget):
    """It is a class which contains a QLineEdit class. Allow user to set text on the screen
    
    Params:
        master (WindowView): Class which base is QDialog class, window, where our widget has to be located.
        width (int): the width in pixels of item
        height (int): the height in pixels of item
        position_x (int): Position x of item, if out of window, then throw an error
        position_y (int): Position y of item, if out of window, then throw an error
        font_size (str): Font size of text which will be shown on item
        placeholder (str): Default text which will be shown on item and automatically removed when first letter will be written 
        editing_finished_function (Callable): Optional function which will be invokes when user stopped focusing on the widget
        return_pressed_function (Callable): Optional function which will be invokes when user clicked enter on the widget
        text_changed_function (Callable): Optional function which will be invokes every time when status of text on widget is changed"""

    font_size: int = field(repr=False, default=14)
    placeholder: str = field(repr=False, default="")
    editing_finished_function: Callable = field(repr=False, default=lambda: None)
    return_pressed_function: Callable = field(repr=False, default=lambda: None)
    text_changed_function: Callable = field(repr=False, default=lambda: None)

    def __post_init__(
        self, width: int, height: int, position_x: int, position_y: int, type_name: str
    ) -> None:
        """Initialize a new PhoneAppEntryBox instance"""
        self.widget: QLineEdit = QLineEdit(self._BaseWidget__master)
        super().__post_init__(width, height, position_x, position_y, type_name)
        if self.placeholder:
            self.widget.setPlaceholderText(self.placeholder)
        self.set_font(self.font_size)
        self.widget.editingFinished.connect(lambda: self.editing_finished_function())
        self.widget.returnPressed.connect(lambda: self.return_pressed_function())
        self.widget.textChanged.connect(lambda: self.text_changed_function())

    @property
    def text(self) -> str:
        """Property which provides a text written on QLineEdit

        Returns:
            text from the widget"""
        return self.widget.text()

    @text.setter
    def text(self, new_text: str) -> None:
        """Property setter which set a text on the widget"""
        self.widget.setText(new_text)

    @text.deleter
    def text(self) -> None:
        """Property deleter which remove text from the widget"""
        self.text = ""

    def set_font(self, size: int) -> None:
        """Method which set new font size on QLineEdit

        Params:
            size (int): new font size
            """
        self.widget.setFont(QFont("Helvetica", size))

    @property
    def read_only(self) -> bool:
        """Property which provides reading status of widget
        
        Returns:
            True if user cannot pass any text to widget, otherwise False"""
        return self.widget.isReadOnly()

    @read_only.setter
    def read_only(self, value: bool) -> None:
        """Property setter which set reading status of widget"""
        self.widget.setReadOnly(value)
