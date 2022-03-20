from re import MULTILINE
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from brute import brute_force
from kivy.uix.progressbar import ProgressBar


class gui(App):
    def build(self):
        #returns a window object with all it's widgets
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.8, 0.8)
        self.window.pos_hint = {"center_x": 0.5, "center_y":0.5}
        self.title = "Recover your wallet"

        # label widget
        self.t = Label(
                        text= "Recover Your Seed Phrase",
                        font_size= 38,
                        color= '#F2F3F5'
                        )
        self.window.add_widget(self.t)

        self.seed = Label(
                        text= "Insert your seed phrase:",
                        font_size= 24,
                        color= '#F2F3F5'
                        )
        self.window.add_widget(self.seed)

        # text input widget
        self.user_seed = TextInput(
                    multiline= False,
                    font_size = 20,
                    size_hint= (1, 0.5)
                    )

        self.window.add_widget(self.user_seed)

        self.address = Label(
                        text= "Insert your address:",
                        font_size= 24,
                        color= '#F2F3F5'
                        )
        self.window.add_widget(self.address)

        # text input widget
        self.user_address = TextInput(
                    multiline= False,
                    font_size = 20,
                    size_hint= (1, 0.5)
                    )

        self.window.add_widget(self.user_address)

        # button widget
        self.button = Button(
                      text= "START",
                      size_hint= (1,0.5),
                      padding = (15,15),
                      bold= True,
                      background_color ='#00FF00'
                      )

        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)
        self.window.add_widget(Label(text=""))

        self.result = TextInput(
                        readonly = True,
                        text= "",
                        multiline= False,
                        font_size = 16,
                        size_hint= (1, 0.5)
                        )
        
        self.window.add_widget(self.result)

        return self.window

    def callback(self, instance):
        # change label text to "Hello + user name!"
        with open('../en.txt') as f:
            words = f.read().splitlines()

        result = brute_force(self.user_seed.text, words, self.user_address.text)
        self.result.text = result

# run Say Hello App Calss
if __name__ == "__main__":
    gui().run()

