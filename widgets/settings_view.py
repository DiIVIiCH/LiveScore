import os

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import ObjectProperty, ListProperty
from kivy.uix.settings import Settings, InterfaceWithNoMenu, SettingItem
from kivy.uix.label import Label
from libs.kivymd.dialog import MDDialog
from libs.kivymd.textfields import MDTextField 
from libs.kivymd.label import MDLabel
from kivy.core.window import Window
from kivy.compat import string_types, text_type
root = os.path.split(__file__)[0]
root = root if root != '' else os.getcwd()
Builder.load_file('{}/kv/settings_view.kv'.format(root))

class LiveScoreSettingString(SettingItem):
    popup = ObjectProperty(None, allownone=True)
    '''(internal) Used to store the current popup when it's shown.

    :attr:`popup` is an :class:`~kivy.properties.ObjectProperty` and defaults
    to None.
    '''

    textinput = ObjectProperty(None)
    '''(internal) Used to store the current textinput from the popup and
    to listen for changes.

    :attr:`textinput` is an :class:`~kivy.properties.ObjectProperty` and
    defaults to None.
    '''

    def on_panel(self, instance, value):
        if value is None:
            return
        self.fbind('on_release', self._create_popup)

    def _dismiss(self, *largs):
        if self.textinput:
            self.textinput.focus = False
        if self.popup:
            self.popup.dismiss()
        self.popup = None

    def _validate(self, instance):
        self._dismiss()
        value = self.textinput.text.strip()
        self.value = value

    def _create_popup(self, instance):
        # create popup layout
        content = BoxLayout(orientation='vertical', spacing='5dp')
        popup_width = min(0.95 * Window.width, 500)        

        # create the textinput used for numeric input
        self.textinput = textinput = MDTextField(
            text=self.value, font_size='24sp', multiline=False,
            size_hint_y=None, height='42sp')
       
        self.popup = popup = MDDialog(
            title=self.title, content=textinput, size_hint=(None, None),
            size=(popup_width, '250dp'))
        self.textinput = textinput
        popup.add_action_button("Cancel",
                                      action=self._dismiss)
        popup.add_action_button("OK",
                                      action=self._validate)

        
        # all done, open the popup !
        popup.open()

class LiveScoreSettingNumeric(LiveScoreSettingString):
    def _validate(self, instance):
        # we know the type just by checking if there is a '.' in the original
        # value
        is_float = '.' in str(self.value)
        self._dismiss()
        try:
            if is_float:
                self.value = text_type(float(self.textinput.text))
            else:
                self.value = text_type(int(self.textinput.text))
        except ValueError:
            return

class LiveScoreSettingBoolean(SettingItem):  
    values = ListProperty(['0', '1'])

class LiveScoreSettingsInterface(InterfaceWithNoMenu):  
    pass

class LiveScoreSettings(Settings):  
    def __init__(self, **kwargs):
        super(LiveScoreSettings, self).__init__(**kwargs)
        self.register_type('bool', LiveScoreSettingBoolean)
        self.register_type('numeric', LiveScoreSettingNumeric)

    def add_kivy_panel(self):
        pass

