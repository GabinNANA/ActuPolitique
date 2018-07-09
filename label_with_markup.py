# -*- coding: cp1252 -*-
from kivy.app import App
from kivy.lang import Builder

root = Builder.load_string('''
BoxLayout:
    canvas.before:
        Color:
            rgba: 1, 1,2, 0.97
        Rectangle:
            pos: self.pos
            size: self.size
    orientation: 'vertical'
    padding: 90
    Label:
        text:
            ('[b][color=000010]Actu[/color] [color=008080]Politique[/color][/b]\\n'
            )
        markup: True
        font_size: '64pt'
    Label:
        text:
            ("[color=000010]Toute l'actualité...[/color]\\n"
            "[color=000010]                     Pour votre seul plaisir[/color]\\n"
            )
        markup: True
        font_size: '30pt'
''')


class LabelWithMarkup(App):
    def build(self):
        return root


if __name__ == '__main__':
    LabelWithMarkup().run()
