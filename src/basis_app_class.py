from dataclasses import InitVar, dataclass, field
from typing import Protocol, Type, overload
from PyQt5.QtWidgets import QApplication, QStackedWidget
from .singleton import Singleton


class PhoneApp(Protocol):
    """The protocol class created to make the earlier declaration of PhoneApp class"""

    @property
    def width(self) -> int:
        """Protocol property which basically returns a width of app"""
        ...

    @property
    def height(self) -> int:
        """Protocol property which basically returns a height of app"""
        ...



@dataclass
class WindowView(Protocol):
    """The Protocol class which performs the function of every window of application.

    Params:
        master (PhoneApp): base component of the whole app"""

    master: PhoneApp


@dataclass
class PhoneApp(metaclass=Singleton):
    """Singleton class which is basis for the entire app.

    Params:
        master (QApplication): main component of PyQt5 app, the __str__ method doesn't contain this variable
        title (str): title of PhoneApp application
        style_file (str): name of css file which contains all stylesheets of widgets
        first_window (Type[WindowView]): class object which is shown when app is turned on
        height (int): height of the window, property which is initialized during the __post_init__ method
        width (int): width of the window, property which is initialized during the __post_init__ method
        widget (QStackedWidget): component which will contain every view of application, the __str__ method doesn't contain this variable and user cannot initialize it
        _windows (dict): initially empty dictionary which will contain every class as key and every instance of this class as a value, the __str__ method doesn't contain this variable and user cannot initialize it"""

    master: QApplication = field(repr=False)
    title: str
    style_file: str
    first_window: Type[WindowView]
    initial_height: InitVar[int]
    initial_width: InitVar[int]
    widget: QStackedWidget = field(init=False, repr=False)
    _windows: dict = field(init=False, repr=False)

    def __post_init__(self, screen_width: int, screen_height: int) -> None:
        """Initialize a new PhoneApp instance

        Params:
            screen_widht (int): width of app
            screen_height (int): height of app"""
        self.widget = QStackedWidget()
        with open(f"src/{self.style_file}") as style_file:
            self.master.setStyleSheet(style_file.read())
        self._windows = {}
        self.add_set_widget(self.first_window, screen_width, screen_height)
        self.widget.show()

    @property
    def height(self) -> int:
        """Property which provides a height of app

        Returns:
            height of the app"""
        return self.widget.height()

    @property
    def width(self) -> int:
        """Property which provides a width of app

        Returns:
            width of the app"""
        return self.widget.width()

    @height.setter
    def height(self, new_height: int) -> None:
        """Setter which sets new height of app"""
        self.widget.setFixedHeight(new_height)

    @width.setter
    def width(self, new_width: int) -> None:
        """Setter which sets new width of app"""
        self.widget.setFixedWidth(new_width)

    def set_measures(self, new_width: int = 0, new_height: int = 0) -> None:
        """Method which sets new height and width of app

        Params:
            widht (int): new widht of app window
            height (int): new height of app window"""
        if new_width:
            self.width = new_width
        if new_height:
            self.height = new_height

    def add_widget(self, new_widget: Type[WindowView]) -> None:
        """Method which adds new class object to the dictionary, if dictionary already contains this class, it is replaced with a new one

        Params:
            widget (Type[WindowView]): class object which is setted on current widget"""
        widget = new_widget(self)
        if self._windows.get(new_widget.__name__):
            del self._windows[new_widget.__name__]
        self._windows[new_widget.__name__] = widget
        self.widget.addWidget(widget)
    @overl
    def set_widget(self, widget: Type[WindowView], width: int, height: int) -> None:
        """Method which sets new class object on current widget

        Params:
            widget (Type[WindowView]): class object which is setted on current widget
            widht (int): new widht of app window, if not passed, then it wouldn't change the width
            height (int): new height of app window, if not passed, then it wouldn't change the height"""
        self.set_measures(width, height)
        name = widget.__name__
        self.widget.setCurrentWidget(self._windows.get(name))
    @overload
    def set_widget(self, widget: Type[WindowView]) -> None:
        """Method which sets new class object on current widget

        Params:
            widget (Type[WindowView]): class object which is setted on current widget"""
        name = widget.__name__
        self.widget.setCurrentWidget(self._windows.get(name))


    def add_set_widget(
        self, new_widget: Type[WindowView], width: int = 0, height: int = 0
    ) -> None:
        """Method which adds new class object to the dictionary and also sets it as current widget, if dictionary already contains this class, it is replaced with a new one

        Params:
            widget (Type[WindowView]): class object which added to dictionary and setted on current widget
            widht (int): new widht of app window, if not passed, then it doesn't change the width
            height (int): new height of app window, if not passed, then it doesn't change the height"""
        self.set_measures(width, height)
        self.add_widget(new_widget)
        self.set_widget(new_widget)

