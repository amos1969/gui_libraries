from tkinter import Toplevel
from guizero import App
from guizero import Text
from guizero import PushButton


class PunchLine(Toplevel):
    def __init__(self, original):
        self.original_frame = original
        # Call the constructor for the Toplevel tk object, which this inherits from
        super().__init__()
        # Set up the GUI
        self.geometry("400x100")
        self.title("Punch Line")
        self.layout_manager = "auto"
        self.some_text = Text(self, "You can't wash your hands in a buffalo!", color="white")
        self.close_button = PushButton(self, text="Close", command=self.close)
        self.quit_button = PushButton(self, text="Quit", command=self.quit)

    def close(self):
        # When we click close, destroy this window and open the original main window
        # that was referenced when we created this one
        self.destroy()
        self.original_frame.show()


class MainWindow:
    def __init__(self, master):
        self.master = master
        self.instructions = Text(self.master, "What's the difference between a Buffalo and a Bison?", color="white")
        self.button = PushButton(self.master, text="Punch Line", command=self.punch_line)

    def punch_line(self):
        # Hide this window
        self.master.withdraw()
        # Create a new instance of the Punch Line Window and pass it a reference to this window
        PunchLine(self)

    def show(self):
        # Update any widgets
        self.master.update()
        # Un-withdraw the hidden window
        self.master.deiconify()


app = App(title="Tell me a joke", width=400, height=100)
some_window = MainWindow(app)
app.display()
