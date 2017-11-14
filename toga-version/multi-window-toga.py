import toga
import sys

class JokeWindow(toga.App):
    def startup(self):
        self.main_window = toga.MainWindow("Joke Window")
        self.main_window.app = self
        self.label = toga.Label("What's the difference between a buffalo and a bison?")
        self.label.style.set(margin=30)
        self.punch_line_button = toga.Button("Punch Line", on_press=self.open_punch_line_window)
        self.punch_line_button.style.set(margin=20)
        self.box = toga.Box(children=[self.label, self.punch_line_button])
        self.main_window.content = self.box
        self.main_window.show()

    def open_punch_line_window(self, *args, **kwargs):
        self.punch_line_window = PunchLine("Punch Line Window")


class PunchLine():

    def __init__(self, name):
        self.child_window = toga.Window(title=name)
        self.label = toga.Label("You can't wash your hands in a Buffalo!")
        self.label.style.set(margin=30)
        self.okay_button = toga.Button("Okay", on_press=self.okay_button_pressed)
        self.okay_button.style.set(margin=15)
        self.close_button = toga.Button("Close", on_press=self.close_button_pressed)
        self.close_button.style.set(margin=15)
        self.box = toga.Box(children=[self.label, self.okay_button, self.close_button])
        self.child_window.content = self.box
        self.child_window.show()

    def okay_button_pressed(self, *args, **kwargs):
        self.child_window.close()

    def close_button_pressed(self, *args, **kwargs):
        sys.exit()

if __name__ == '__main__':
    app = JokeWindow(
        'Joke Window',
        'net.dave-ames.joker'
    )
    app.main_loop()
