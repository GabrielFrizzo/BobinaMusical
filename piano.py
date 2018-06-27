from kivy.config import Config

#Config.set("input", "mouse", "mouse,disable_multitouch")
#Config.set('graphics', 'width', '405')
#Config.set('graphics', 'height', '720')
#Config.set('graphics', 'resizable', '0') # Trava o resize da janela
#Config.set('graphics', 'show_cursor', '0')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.loader import Loader
#from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
#from kivy.uix.scatter import Scatter
#from kivy.uix.behaviors import FocusBehavior
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.slider import Slider
from kivy.factory import Factory
from kivy.logger import Logger
from kivy.lang import Builder
from kivy.graphics import Color
from kivy.graphics import Rectangle
from kivy.graphics import Line
from kivy.graphics import Ellipse
from kivy.vector import Vector
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
from kivy.garden.mapview import MapView # https://github.com/kivy-garden/garden.mapview
from kivy.animation import Animation
from functools import partial
from kivy.uix.behaviors import ButtonBehavior
import random




class MyScreenManager(ScreenManager):
    returned = False

class TopOfEverything(FloatLayout):
    window_size = [383,680]
    
    def __init__(self, *args, **kwargs):
        super(TopOfEverything, self).__init__(*args, **kwargs)
        self.keyboard_setup()


    ### Keyboard para debug
    def keyboard_setup(self,me=None,*args):
        if me == None:
            me = self
        me._keyboard = Window.request_keyboard(me._keyboard_closed, me)
        me._keyboard.bind(on_key_down=me._on_keyboard_down)
            
    def _keyboard_closed(self):
        pass

    def _on_keyboard_down(self,keyboard,keycode,text,modifiers):
        pass

    def on_touch_up(self, touch):
        print("POS", touch.pos[0]/800)


class MainMenu(Screen):
    def __init__(self, *args, **kwargs):
        super(MainMenu, self).__init__(*args, **kwargs)
        Clock.schedule_once(self.create_keyboard, 1)
        self.keyboard = []
        
    def create_keyboard(self, *args):

        piano = self.ids.piano_image
        
        # Limpa todas as teclas para criar novas quando se redimensiona a tela.
        for key in self.keyboard:
            self.remove_widget(key)

        # Teclas brancas
        key_size = (piano.size[0]*.97 / 36, piano.size[1] * 0.23)
        start_x = piano.pos[0] + .015 * piano.size[0]
        i = 0
        while i < 36:
            new_button = PButton(pos=(start_x + i*key_size[0], 0),
                                 size=(key_size),
                                 size_hint=(None, None),
                                 idx=i+1)
            i += 1
            self.keyboard.append(new_button)
            self.add_widget(new_button)

        # Teclas pretas
        black_key_size = (key_size[0]*.6, key_size[1]*1.6)
        black_key_pos = [.0325, .06375, .1125, .1425, .1725,
                         .22125, .2525, .30125, .33125, .3625,
                         .41, .44125, .48875, .52, .55,
                         .5975, .63, .6775, .7075, .7375,
                         .785, .8175, .86375, .895, .925]
        i = 0
        while i < 25:
            new_button = PButton(pos=(black_key_pos[i]*self.width, key_size[1]),
                                 size=(black_key_size),
                                 size_hint=(None, None),
                                 idx=37+i)
            i += 1
            self.keyboard.append(new_button)
            self.add_widget(new_button)
        

        

        
            
        

class PButton(ButtonBehavior, Widget):
    def __init__(self, **kwargs):
        self.idx = kwargs['idx']
        del(kwargs['idx'])
        super(PButton, self).__init__(**kwargs)

        with self.canvas:
            Color(random.random(), random.random(), random.random(), 1)
            self.rect = Rectangle(pos=self.pos,
                                  size=self.size)
                        
    def key_press(self):
        print("Key", self.idx, "pressed.")




####################

class TecladoBluetooth(App):
    def build(self):
        return TopOfEverything()

      
with open("layout.kv", "rb") as kvfile:
    kivystr = kvfile.read()
    Builder.load_string(kivystr.decode('cp1252'))

    
if __name__ == "__main__":
    TecladoBluetooth().run()
