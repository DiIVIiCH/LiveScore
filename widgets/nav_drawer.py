import os

from kivymd.navigationdrawer import MDNavigationDrawer, NavigationDrawerHeaderBase
from kivy.lang import Builder
from kivy.properties import ObjectProperty, NumericProperty, ListProperty
from kivymd.list import BaseListItem
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.elevationbehavior import RectangularElevationBehavior

root = os.path.split(__file__)[0]
root = root if root != '' else os.getcwd()
Builder.load_file('{}/kv/nav_drawer.kv'.format(root))

class NavDrawer(BoxLayout, ThemableBehavior, RectangularElevationBehavior):
    '''
    '''
    _elevation = NumericProperty(0)
    _header_container = ObjectProperty()
    _list = ObjectProperty()
    active_item = ObjectProperty(None)
    orientation = 'horizontal'
    panel = ObjectProperty()
    shadow_color = ListProperty([0, 0, 0, 0])

    def __init__(self, **kwargs):
        super(NavDrawer, self).__init__(**kwargs)

    def add_widget(self, widget, index=0):
        '''
        If the widget is a subclass of :class:`~NavigationDrawerHeaderBase`, then it will be placed above the
        :class:`~kivy.uix.scrollview.ScrollView`. Otherwise, it will be placed in the main
        :class:`~kivy.uix.scrollview.ScrollView` content area.
        '''
      
        super(NavDrawer, self).add_widget(widget, index)

