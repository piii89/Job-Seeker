from UI_modules import *
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.effects.dampedscroll import DampedScrollEffect
from kivy.uix.textinput import TextInput
from kivy.config import Config

Config.set('input', 'mouse', 'mouse,multitouch_on_demand')


class WindowManager(ScreenManager):
    pass


class IntroWindow(Screen):
    user_input1 = ObjectProperty(None)


class MainWindow(Screen):
    user_input = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)

    @ classmethod
    def return_results(self):
        return olx(self.user_input)
        # if IntroWindow().user_input1 == "olx":
        #     return olx(self.user_input)
        # elif IntroWindow().user_input1 == "pracuj":
        #     return pracuj(self.user_input)
        # elif IntroWindow().user_input1 == "gumtree":
        #     return gumtree(self.user_input)
        # elif IntroWindow().user_input1 == "all":
        #     return res_all(self.user_input)


class scrolling(DampedScrollEffect):
    def __init__(self, **kwargs):
        super(scrolling, self).__init__(**kwargs)
        self.spring_constant = 0


class ResultsWindow(Screen):
    def __init__(self, **kwargs):
        super(ResultsWindow, self).__init__(**kwargs)

        self.scroller = ScrollView(effect_cls=scrolling)
        self.grid = GridLayout(
            cols=1, row_default_height='110dp', row_force_default=True, spacing=0, padding=0, size_hint_y=None)
        self.res_list1 = MainWindow().return_results()
        for i in self.res_list1:
            self.grid.add_widget(Label(text=' '.join(
                i), font_size=15, text_size=(1000, None), size_hint_y=None))
        self.scroller.add_widget(self.grid)
        self.add_widget(self.scroller)


kv = Builder.load_file("js.kv")


class JobSeek(App):
    def build(self):
        return kv


if __name__ == "__main__":
    JobSeek().run()
