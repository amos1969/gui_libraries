import tkinter as tk

class PunchLine(tk.Toplevel):

    def __init__(self, original):
        # Set a reference to the original Main Window which created this one
        self.original_frame = original
        # Call the constructor for the Toplevel tk object, which this inherits from
        super().__init__()
        # Set up the GUI
        self.geometry("400x100")
        self.title("Child One Window")
        self.main_label = tk.Label(self, text="You can't wash your hands in a buffalo!")
        self.main_label.pack()
        self.close_button = tk.Button(self, text="Close", command=self.close)
        self.close_button.pack()
        self.quit_button = tk.Button(self, text="Quit", command=self.quit)
        self.quit_button.pack()

    def close(self):
        # When we click close, destroy this window and open the original main window
        # that was referenced when we created this one
        self.destroy()
        self.original_frame.show()


class MainWindow:

    def __init__(self, master):
        self.master = master
        self.master.title("Main Window")
        self.frame = tk.Frame(self.master)
        self.frame.pack()
        self.my_label = tk.Label(self.frame, text="What's the difference between a Buffalo and a Bison?")
        self.my_label.pack()
        self.first_window_button = tk.Button(self.frame, text="Punch Line", command=self.open_punch_line_window)
        self.first_window_button.pack()

    def open_punch_line_window(self):
        # Hide this window
        self.master.withdraw()
        # Create a new instance of the Punch Line Window and pass it a reference to this window
        PunchLine(self)

    def show(self):
        # Update any widgets
        self.master.update()
        # Un-withdraw the hidden window
        self.master.deiconify()


def main():
    root = tk.Tk()
    root.geometry("400x100")
    MainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
