from typing import Any, Dict, Protocol, Type, overload
from PyQt5.QtWidgets import QTabWidget, QWidget
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt
from dataclasses import dataclass
from .basis_app_class import PhoneApp


@dataclass
class TabWidget(Protocol):
    """Tab Widget class which is base class to which will be added all of the tab components..."""

    ...


class BaseTab(Protocol):
    """Basic component for every tab class instance
    
    Params:
        title (str): unique title of tab
        master (TabWidget): base component to which are added every tab instance
        type_name (str): object name which is used to getting styleshit"""

    title: str
    master: TabWidget
    type_name: str = ""

    def remove(self) -> None:
        """Method which directly remove tab from tab bar."""
        ...

    @property
    def title(self) -> str:
        """Property which provides title of tab
        
        Returns:
            title of tab"""
        ...

    @title.setter
    def title(self, new_title: str) -> None:
        """Property setter which set new title of tab
        
        Params: 
            new_title (str): new title of tab"""
        ...

    @property
    def type_name(self) -> str:
        """Property which provides an object name
        
        Returns:
            name of widget"""
        ...

    @type_name.setter
    def type_name(self, name: str) -> None:
        """Property setter which set an object name
        
        Params:
            name (str): new name of widget"""
        ...

    @type_name.deleter
    def type_name(self) -> None:
        """Property deleter which remove an object name"""
        ...


class TabClass(BaseTab, Protocol):
    """Class which inherited from Base Tab class"""

    ...


class TabWidget(QTabWidget):
    """Tab Widget class which is base class to which will be added all of the tab components"""

    def __init__(self, master: PhoneApp, type_name: str = "") -> None:
        """Initialize instance of class
        
        Params:
            master (PhoneApp): base of whole phone application
            type_name (str): object name which is used to getting stylesheet"""
        super().__init__()
        self.__master = master
        self.tabs: Dict[str, TabClass] = {}
        if type_name:
            self.type_name = type_name
        self.tabBar().setCursor(QCursor(Qt.OpenHandCursor))
        # self.add_tab(First, "okno")
        self.setUsesScrollButtons(False)

    def __set_size(self) -> None:
        width = self.__master.width
        try:
            width = int((width - 50) / len(self.tabs))
            if width > 250:
                width = 150
            self.setStyleSheet("QTabBar::tab{width: %spx}" % width)
        except ZeroDivisionError:
            ...  # here should be something which inform programist about implementation of tabbar with zero tabs

    @property
    def type_name(self) -> str:
        """Property which provides an object name
        
        Returns:
            name of widget"""
        return self.objectName()

    @type_name.setter
    def type_name(self, name: str) -> None:
        """Property setter which set an object name
        
        Params:
            name (str): new name of widget"""
        self.setObjectName(name)

    @type_name.deleter
    def type_name(self) -> None:
        """Property deleter which remove an object name"""
        self.setObjectName("")

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
                tab = widget_class(self, name, type_name, **kwargs)
            else:
                tab = widget_class(self, name, **kwargs)
            if isinstance(index, int):
                self.insertTab(index, tab, name)
            else:
                self.addTab(tab, name)
            self.tabs[name] = tab
            self.__set_size()
            return tab
        else:
            ...  # here should be something which inform programmist about the unintented behaviour of the program

        return tab

    def remove_tab(self, name: str) -> None:
        """Method which removed tab from tab bar based on its unique title

        Params:
            name (str): title of tab"""
        if name in self.tabs:
            tab = self.tabs.pop(name)
            self.removeTab(self.indexOf(tab))


class BaseTab(QWidget):
    """Basic component for every tab class instance"""

    def __init__(self, master: TabWidget, title: str, type_name: str = "") -> None:
        """Method which helps with creating Tab instance
        
        Params:
            title (str): unique title of tab
            master (TabWidget): base component to which are added every tab instance
            type_name (str): object name which is used to getting styleshit"""
        self.__master = master
        self.__title = title
        super().__init__(self.__master)
        if type_name:
            self.type_name = type_name

    def remove(self) -> None:
        """Method which directly remove tab from tab bar."""
        self.__master.remove_tab(self.title)
        self.destroy(True)

    @property
    def title(self) -> str:
        """Property which provides title of tab
        
        Returns:
            title of tab"""
        return self.__title

    @title.setter
    def title(self, new_title: str) -> None:
        """Property setter which set new title of tab
        
        Params:
            new_title (str): new title of tab"""
        keys = list(self.__master.tabs.keys())
        index = keys.index(self.title)
        keys[index] = new_title
        self.__title = new_title
        self.__master.tabs = {
            key: value for key, value in zip(keys, self.__master.tabs.values())
        }
        self.__master.insertTab(index, self, new_title)

    @property
    def type_name(self) -> str:
        """Property which provides an object name
        
        Returns:
            name of widget"""
        return self.objectName()

    @type_name.setter
    def type_name(self, name: str) -> None:
        """Property setter which set an object name
        
        Params:
            name (str): new name of widget"""
        self.setObjectName(name)

    @type_name.deleter
    def type_name(self) -> None:
        """Property deleter which remove an object name"""
        self.setObjectName("")


# todo: remove in the future, it is only a visualation how should tab class look, its protocol is tabclass
class First(BaseTab):
    """Tab class"""

    def __init__(
        self, master: TabWidget, title: str, type_name: str = "", **kwargs
    ) -> None:
        """Method which create Tab instance"""
        super().__init__(master, title, type_name)

