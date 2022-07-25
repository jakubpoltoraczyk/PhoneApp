from typing import Any, Dict, Protocol, Type, overload
from PyQt5.QtWidgets import QTabWidget, QWidget
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt
from dataclasses import dataclass, field
from .basis_app_class import PhoneApp


@dataclass
class TabWidget(Protocol):
    """Tab Widget class which is base class to which will be added all of the tab components..."""

    ...


@dataclass
class Tab(Protocol):
    """Basic component for every tab class instance
    
    Params:
        title (str): unique title of tab
        master (TabWidget): base component to which are added every tab instance
        type_name (str): object name which is used to getting styleshit"""

    title: str
    master: TabWidget
    type_name: str = field(default="")

    def __post_init__(self) -> None:
        """Method which helps with creating Tab instance"""
        ...

    def remove(self) -> None:
        """Method which directly remove tab from tab bar."""
        ...


@dataclass
class TabClass(Tab, Protocol):
    kwargs: dict = field(default_factory={})

    def __post_init__(self) -> None:
        super().__post_init__()
        ...


@dataclass
class TabWidget(Protocol):
    """Tab Widget class which is base class to which will be added all of the tab components
    
    Params:
        master (PhoneApp): base of whole phone application
        ..."""

    master: PhoneApp
    ...

    @overload
    def add_tab(self, widget_class: Type[TabClass], name: str, **kwargs) -> None:
        """Method which add new tab based on defined index without passing type name

        Params:
            name (str): title of tab"""
        ...

    @overload
    def add_tab(
        self,
        widget_class: Type[TabClass],
        name: str,
        index: int,
        type_name: str = "",
        **kwargs
    ) -> None:
        """Method which add new tab based on defined index with defined type name

        Params:
            name (str): title of tab
            type_name (str): object name which is used to getting stylesheet
            index (int): position of tab"""
        ...

    @overload
    def add_tab(
        self, widget_class: Type[TabClass], name: str, type_name: str = "", **kwargs
    ) -> None:
        """Method which add new tab on last place with defined type name

        Params:
            name (str): title of tab
            type_name (str): object name which is used to getting styleshit"""
        ...

    def add_tab(
        self,
        widget_class: Type[TabClass],
        name: str,
        index: int = ...,
        type_name: str = ...,
        **kwargs
    ) -> None:
        """Method which add new tab to the tab bar
        
        Params:
            name (str): title of tab
            type_name (str): object name which is used to getting styleshit
            index (int): position of tab"""
        ...

    def remove_tab(self, name: str) -> None:
        """Method which removed tab from tab bar based on its unique title

        Params:
            name (str): title of tab"""
        ...


@dataclass
class Tab(QWidget):
    """Basic component for every tab class instance
    
    Params:
        title (str): unique title of tab
        master (TabWidget): base component to which are added every tab instance
        type_name (str): object name which is used to getting styleshit"""

    title: str
    master: TabWidget
    type_name: str = field(default="")

    def __post_init__(self) -> None:
        """Method which helps with creating Tab instance"""
        super().__init__(self.master)

    def remove(self) -> None:
        """Method which directly remove tab from tab bar."""
        self.master.remove_tab(self.title)
        self.destroy(True)


# todo: remove in the future, it is only a visualation how should tab class look
@dataclass
class First(Tab):
    """Tab class"""

    def __post_init__(self) -> None:
        """Method which create Tab instance"""
        super().__post_init__()


@dataclass
class TabWidget(QTabWidget):
    """Tab Widget class which is base class to which will be added all of the tab components
    
    Params:
        master (PhoneApp): base of whole phone application
        type_name (str): object name which is used to getting stylesheet"""

    master: PhoneApp
    type_name: str = field(default="")

    def __post_init__(self) -> None:
        """Initialize instance of class"""
        super().__init__()
        self.tabs: Dict[str, Tab] = {}
        if self.type_name:
            self.setObjectName(self.type_name)
        self.tabBar().setCursor(QCursor(Qt.OpenHandCursor))
        self.setUsesScrollButtons(False)

    def __set_size(self) -> None:
        width = self.master.width
        try:
            width = int((width - 50) / len(self.tabs))
            if width > 250:
                width = 150
            self.setStyleSheet("QTabBar::tab{width: %spx}" % width)
        except ZeroDivisionError:
            ...  # here should be something which inform programist about implementation of tabbar with zero tabs

    @overload
    def add_tab(
        self, widget_class: Type[TabClass], name: str, **kwargs: Dict[str, Any]
    ) -> TabClass:
        """Method which add new tab based on defined index without passing type name

        Params:
            name (str): title of tab
            kwargs (Dict[str, Any]): rest of the arguments, have to be a default arguments, which are used to initialize new tab
        
        Returns: 
            created instance of new tab or None if creation is impossible"""
        ...

    @overload
    def add_tab(
        self,
        widget_class: Type[TabClass],
        name: str,
        index: int,
        type_name: str = "",
        **kwargs: Dict[str, Any]
    ) -> TabClass:
        """Method which add new tab based on defined index with defined type name

        Params:
            name (str): title of tab
            type_name (str): object name which is used to getting stylesheet
            index (int): position of tab
            kwargs (Dict[str, Any]): rest of the arguments, have to be a default arguments, which are used to initialize new tab
        
        Returns: 
            created instance of new tab or None if creation is impossible"""
        ...

    @overload
    def add_tab(
        self,
        widget_class: Type[TabClass],
        name: str,
        type_name: str = "",
        **kwargs: Dict[str, Any]
    ) -> TabClass:
        """Method which add new tab on last place with defined type name

        Params:
            name (str): title of tab
            type_name (str): object name which is used to getting styleshit
            kwargs (Dict[str, Any]): rest of the arguments, have to be a default arguments, which are used to initialize new tab
        
        Returns: 
            created instance of new tab or None if creation is impossible"""
        ...

    def add_tab(
        self,
        widget_class: Type[TabClass],
        name: str,
        index: int = ...,
        type_name: str = ...,
        **kwargs: Dict[str, Any]
    ) -> TabClass or None:
        """Method which add new tab to the tab bar
        
        Params:
            name (str): title of tab
            type_name (str): object name which is used to getting stylesheet
            index (int): position of tab
            kwargs (Dict[str, Any]): rest of the arguments, have to be a default arguments, which are used to initialize new tab
            
        Returns: 
            created instance of new tab or None if creation is impossible"""

        if name not in self.tabs:
            if isinstance(type_name, str):
                tab = widget_class(name, self, type_name, **kwargs)
            else:
                tab = widget_class(name, self, **kwargs)
            if isinstance(index, int):
                self.insertTab(index, tab, name)
            else:
                self.addTab(tab, name)
            self.tabs[name] = tab
            self.__set_size()
            return tab
        else:
            ...  # here should be something which inform programmist about the unintented behaviour of the program

    def remove_tab(self, name: str) -> None:
        """Method which removed tab from tab bar based on its unique title

        Params:
            name (str): title of tab"""
        if name in self.tabs:
            tab = self.tabs.pop(name)
            self.removeTab(self.indexOf(tab))

