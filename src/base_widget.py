from abc import ABC, abstractmethod
from dataclasses import InitVar, dataclass, field
from PyQt5.QtWidgets import QWidget
from typing import Protocol
from .basis_app_class import WindowView


class BaseForCustomWidget(Protocol):
    @property
    def position_y(self) -> int:
        """Protocol property which provides a position y of widget

        Returns:
            position y of widget"""
        ...

    @property
    def position_x(self) -> int:
        """Protocol property which provides a position x of widget

        Returns:
            position y of widget"""
        ...

    @property
    def width(self) -> int:
        """Protocol property which provides a width of widget

        Returns:
            width of widget"""
        ...

    @property
    def height(self) -> int:
        """Protocol property which provides a height of widget

        Returns:
            height of widget"""
        ...


@dataclass
class CustomWidget(BaseForCustomWidget, Protocol):
    ...

    def __post_init__(self):
        self.widget: QWidget
        ...


@dataclass
class BaseWidget(ABC):
    """It is a class which is base for every class which contains screen components.
    
    Params:
        __master (WindowView): Class which base is QDialog class, window, where our widget has to be located.
        _width (int): the width in pixels of item
        _height (int): the height in pixels of item
        _position_x (int): Position x of item, if out of window, then throw an error
        _position_y (int): Position y of item, if out of window, then throw an error"""

    __master: WindowView
    _width: InitVar[int]
    _height: InitVar[int]
    _position_x: InitVar[int]
    _position_y: InitVar[int] = field(default=2)
    _type_name: InitVar[str] = field(default="")

    @abstractmethod
    def __post_init__(
        self: CustomWidget,
        width: int,
        height: int,
        position_x: int,
        position_y: int,
        type_name: str,
    ):
        self.widget.setGeometry(position_x, position_y, width, height)
        if type_name:
            self.widget.setObjectName(type_name)

    @property
    def width(self: CustomWidget) -> int:
        """Property which provides a width of widget

        Returns:
            width of widget"""
        return self.widget.width()

    @width.setter
    def width(self: CustomWidget, new_width: int) -> None:
        """Property setter which set a new width of widget

        Params:
            new_width (int): new width of widget"""
        self.widget.setGeometry(
            self.position_x, self.position_y, new_width, self.height
        )

    @property
    def height(self: CustomWidget) -> int:
        """Property which provides a height of application

        Returns:
            height of application"""
        return self.widget.height()

    @height.setter
    def height(self: CustomWidget, new_height: int) -> None:
        """Property setter which set a new height of widget

        Params:
            new_height (int): new height of widget"""
        self.widget.setGeometry(
            self.position_x, self.position_y, self.width, new_height
        )

    @property
    def position_x(self: CustomWidget) -> int:
        """Property which provides a position x of widget

        Returns:
            position x of widget"""
        return self.widget.geometry().x()

    @position_x.setter
    def position_x(self: CustomWidget, new_position: int) -> None:
        """Property setter which set a position x of widget

        Params:
            new_position (int): new x position of widget"""
        self.widget.setGeometry(new_position, self.position_y, self.width, self.height)

    @property
    def position_y(self: CustomWidget) -> int:
        """Property which provides a position y of widget

        Returns:
            position y of widget"""
        return self.widget.geometry().y()

    @position_y.setter
    def position_y(self: CustomWidget, new_position: int) -> None:
        """Property setter which set a position y of widget

        Params:
            new_position (int): new y position of widget"""
        self.widget.setGeometry(self.position_x, new_position, self.width, self.height)

    @property
    def type_name(self: CustomWidget) -> str:
        return self.widget.objectName()

    @type_name.setter
    def type_name(self: CustomWidget, name: str) -> None:
        self.widget.setObjectName(name)

    @type_name.deleter
    def type_name(self: CustomWidget) -> None:
        self.widget.setObjectName("")

    def move(
        self: CustomWidget, new_position_x: int = 0, new_position_y: int = 0
    ) -> None:
        """Function which results translating item
        
        Params:
            new_position_x (int): new x position of item
            new_position_y (int): new y position of item
            """
        self.widget.setGeometry(new_position_x, new_position_y, self.width, self.height)
