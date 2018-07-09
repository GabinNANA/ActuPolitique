# -*- coding: cp1252 -*-
import kivy
kivy.require('1.0.7')
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty
from kivy.lang import Builder
from requests import get
from bs4 import BeautifulSoup
from kivy.uix.floatlayout import FloatLayout
import webbrowser


url = 'http://www.lepoint.fr/politique/'
response = get(url)
html_soup = BeautifulSoup(response.text, 'html.parser')
news_containers = html_soup.find_all('div', class_ = 'row keep-cols')
j=str('012')
source= "=========Actualité politique du journal Le Point========="
var="\n\n\n[b][color=008080] [size=30] ACTUALITE POLITIQUE DU JOURNAL LE POINT [/size] [/color][/b]\n"
for i in j:    
    i= int(i)
    first_news = news_containers[i]
    first_name = first_news.h2.text
    first_text = first_news.p.text
    first_lien = 'http://www.lepoint.fr'+first_news.header.a.get('href')
    var = var + '\n' + "[color=000010] [size=30] [b] "+ first_name +" [/b] [/size]" + '\n' + first_text + '\n' + "[/color]"+ "[color=008080][ref=Visiter]" + first_lien + " [/ref][/color] " + '\n'
    i= str('i')
long_text = var

Builder.load_string('''
<lepoint>:
    canvas.before:
        Color:
            rgba: 1, 1,2, 0.97
        Rectangle:
            pos: self.pos
            size: self.size
    Label:
        size_hint_y: None
        height: self.texture_size[1]
        text_size:(600, None)
        line_height:1.5
        text: root.text
        halign: 'justify'
        markup: True
''')

class lepoint(ScrollView):
    
    text = long_text

class lepointApp(App):
    def build(self):
        return ScrollableLabel()

if __name__ == "__main__":
    ScrollApp().run()
