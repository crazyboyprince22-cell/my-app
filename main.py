from kivy.app import App
from kivy.uix.label import Label

class MainApp(App):
    def build(self):
        # Ye label bas tab dikhega agar HTML load nahi ho saki
        return Label(text='App is Loading...')

if __name__ == "__main__":
    MainApp().run(
      
    )
