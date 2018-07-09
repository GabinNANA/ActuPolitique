# -*-coding:Latin-1 -*
import kivy
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
kivy.require('1.0.5')

from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.gesturesurface import GestureSurface
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.multistroke import Recognizer

from scrollable import ScrollableLabel
from label_with_markup import root
from lemonde import lemonde
from lepoint import lepoint
from africain import africain

class Controller(GridLayout):
      pass

class ControllerApp(App):

     def build(self):
        self.manager = ScreenManager(transition=SlideTransition(
                                     duration=.15))
        self.recognizer = Recognizer()
        
        # Setup the GestureSurface and bindings to our Recognizer
        Accueil = root
        Accueil_screen = Screen(name='Accueil')
        Accueil_screen.add_widget(Accueil)
        self.manager.add_widget(Accueil_screen)

        Lefigaro = ScrollableLabel()
        Lefigaro_screen = Screen(name='Lefigaro')
        Lefigaro_screen.add_widget(Lefigaro)
        self.manager.add_widget(Lefigaro_screen)

        LeMonde = lemonde()
        LeMonde_screen = Screen(name='LeMonde')
        LeMonde_screen.add_widget(LeMonde)
        self.manager.add_widget(LeMonde_screen)

        LePoint = lepoint()
        LePoint_screen = Screen(name='LePoint')
        LePoint_screen.add_widget(LePoint)
        self.manager.add_widget(LePoint_screen)

        Africain = africain()
        Africain_screen = Screen(name='Africain')
        Africain_screen.add_widget(Africain)
        self.manager.add_widget(Africain_screen)


        layout = GridLayout(cols=1)
        layout.add_widget(self.manager)
        layout.add_widget(Controller())
        return layout


if __name__ == '__main__':
    ControllerApp().run()
