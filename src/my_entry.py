from dataclasses import dataclass, field
from PyQt5.QtWidgets import QLineEdit, QApplication
from PyQt5.QtGui import QFont, QFontDatabase
from typing import Callable, overload
from .basis_app_class import WindowView



@dataclass
class PhoneAppEntryBox:
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

    master: WindowView
    width: int
    height: int
    _position_x: int
    _position_y: int
    font_size: int = field(repr=False, default=14)
    type_name: str = ""
    placeholder: str = field(repr=False, default="")
    editing_finished_function: Callable = field(repr=False, default=lambda: None)
    return_pressed_function: Callable = field(repr=False, default=lambda: None)
    text_changed_function: Callable = field(repr=False, default=lambda: None)

    def __post_init__(self) -> None:
        """Initialize a new PhoneAppEntryBox instance"""
        self.widget: QLineEdit = QLineEdit(self.master)
        self.position_x = self._position_x
        self.position_y = self._position_y
        self.widget.setGeometry(
            self.position_x, self.position_y, self.width, self.height
        )
        if self.type_name:
            self.widget.setObjectName(self.type_name)
        if self.placeholder:
            self.widget.setPlaceholderText(self.placeholder)
        self.set_font(self.font_size)
        self.widget.editingFinished.connect(lambda: self.editing_finished_function())
        self.widget.returnPressed.connect(lambda: self.return_pressed_function())
        self.widget.textChanged.connect(lambda: self.text_changed_function())

    def move(self, new_position_x: int = 0, new_position_y: int = 0) -> None:
        """Function which results translating item
        
        Params:
            new_position_x (int): new x position of item
            new_position_y (int): new y position of item
            """
        if new_position_x:
            self.position_x = new_position_x
        if new_position_y:
            self.position_y = new_position_y
        self.widget.setGeometry(
            self.position_x, self.position_y, self.width, self.height
        )

    @property
    def position_x(self):
        """Property which provides a position x of widget

        Returns:
            position x of widget"""
        return self._position_x

    @position_x.setter
    def position_x(self, new_position: int) -> None:
        """Property setter which set a position x of widget, raises IndexError when position is out of application box."""
        width = self.master.master.width
        if width >= new_position + self.width and new_position >= 0:
            self._position_x = new_position
        else:
            raise IndexError(
                "Attempt of setting new postion x of item failed"
            )  # todo: i think it would be better if here, instead of raising IndexError, was something which only communicate about incorrect value, now, in this condition, program is stopped

    @property
    def position_y(self) -> None:
        """Property which provides a position y of widget

        Returns:
            position y of widget"""
        return self._position_y

    @position_y.setter
    def position_y(self, new_position: int) -> None:
        """Property setter which set a position y of widget, raises IndexError when position is out of application box."""
        height = self.master.master.height
        if height >= new_position + self.height and new_position >= 0:
            self._position_y = new_position
        else:
            raise IndexError(
                "Attempt of setting new postion y of item failed"
            )  # todo: i think it would be better if here, instead of raising IndexError, was something which only communicate about incorrect value, now, in this condition, program is stopped

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
    
    def set_font(self)
    @overload
    def set_font(self, size: int) -> None:
        """Method which set new font size on QLineEdit"""
        self.widget.setFont(QFont("Helvetica", size))
    
    @overload
    @staticmethod
    def set_font(size: int) -> None:
        """Method which set new font size on every instance of QLineEdit"""
        
        QApplication.setFont(QFont("Helvetica", size), 'QLineEdit')

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

PhoneAppEntryBox.set_font(5)