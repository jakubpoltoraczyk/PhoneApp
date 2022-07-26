from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtGui import QFont
from typing import Any, Callable
from .base_widget import BaseWidget
from .phone_app import WindowView


class MyEntry(BaseWidget):
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

    def __init__(
        self,
        master: WindowView,
        width: int = 100,
        height: int = 30,
        position_x: int = 0,
        position_y: int = 0,
        type_name: str = "",
        font_size: int = 14,
        text: str = "",
        placeholder: str = "",
        read_only: bool = False,
        editing_finished_function: Callable[[], None] = lambda: None,
        return_pressed_function: Callable[[], None] = lambda: None,
        text_changed_function: Callable[[], None] = lambda: None,
    ) -> None:
        """Initialize a new PhoneAppEntryBox instance
        
        Params:
            master (WindowView): Class which base is QDialog class, window, where our widget has to be located.
            width (int): the width in pixels of item
            height (int): the height in pixels of item
            position_x (int): Position x of item, if out of window, then throw an error
            position_y (int): Position y of item, if out of window, then throw an error
            type_name (str): String variable used to create stylesheet of widget
            font_size (str): Font size of text which will be shown on item
            text (str): Text on QLineEdit
            placeholder (str): Default text which will be shown on item and automatically removed when first letter will be written 
            read_only (bool): read only status, when True then user cannot write something on widget
            editing_finished_function (Callable): Optional function which will be invokes when user stopped focusing on the widget
            return_pressed_function (Callable): Optional function which will be invokes when user clicked enter on the widget
            text_changed_function (Callable): Optional function which will be invokes every time when status of text on widget is changed"""
        self.widget: QLineEdit = QLineEdit(master)
        super().__init__(master, width, height, position_x, position_y, type_name)
        if placeholder:
            self.placeholder = placeholder
        if read_only:
            self.read_only = read_only
        if text:
            self.text = text
        self.font_size = font_size
        self.set_editing_finished_function(editing_finished_function)
        self.set_return_pressed_function(return_pressed_function)
        self.set_text_changed_function(text_changed_function)

    def set_editing_finished_function(self, new_function: Callable[[], Any]) -> None:
        """Method which set function which will be invokes when user stopped focusing on the widget
        
        Params:
            new_function (Callable() -> Any): function which will be invokes when user stopped focusing on the widget """
        self.widget.editingFinished.connect(lambda: new_function())

    def set_text_changed_function(self, new_function: Callable[[], Any]) -> None:
        """Method which set function which will be invokes when user clicked enter on the widget
        
        Params:
            new_function (Callable() -> Any): function which will be invokes when user clicked enter on the widget """
        self.widget.textChanged.connect(lambda: new_function())

    def set_return_pressed_function(self, new_function: Callable[[], Any]) -> None:
        """Method which set function which will be invokes every time when status of text on widget is changed
        
        Params:
            new_function (Callable() -> Any): function which will be invokes every time when status of text on widget is changed """
        self.widget.returnPressed.connect(lambda: new_function())

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

    @property
    def placeholder(self) -> str:
        """Property which provides a text written on QLineEdit before padding some text

        Returns:
            placeholder from the widget"""
        return self.widget.placeholderText()

    @placeholder.setter
    def placeholder(self, new_placeholder: str) -> None:
        """Property setter which set a new placeholder on widget"""
        self.widget.setPlaceholderText(new_placeholder)

    @placeholder.deleter
    def placeholder(self) -> None:
        """Property deleter which remove placeholder from widget"""
        self.placeholder = ""

    @property
    def font_size(self) -> int:
        """Property method which provide font size on QLineEdit

        Returns:
            size of widget"""
        return self.widget.font().pointSize()

    @font_size.setter
    def font_size(self, size: int) -> None:
        """Property method which set new font size on QLineEdit

        Params:
            size (int): new font size"""
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
