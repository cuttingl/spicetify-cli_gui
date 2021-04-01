import subprocess
import bat_scripts
try:
    import Tkinter as tk
except:
    import tkinter as tk

class Window(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        tk.Frame(self, width = 200, height = 400)
        self.master.geometry("500x200")
        self.pack()
        self.create_widgets()

    def create_widgets(self):

        self.button_update_spotify = tk.Button(self, 
                text="New Spotify update ! Apply backup to spicetify", 
                command=bat_scripts.update_spotify
                )
        self.button_update_spotify.pack(side="top")

        self.button_update_css= tk.Button(self, 
                text="Update CSS", 
                command=bat_scripts.update_css
                )

        self.button_update_css.pack(side="top")

        self.button_test = tk.Button(self,
                                    text="Restore Spotify to default",
                                    command= bat_scripts.test)
        self.button_test.pack(side="top")  

        self.exit_button = tk.Button(self,
                text="Exit",
                fg="white",
                bg = "red",
                command=self.master.destroy)
        self.exit_button.pack(side="bottom")