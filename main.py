import Window as window
import os

if __name__ == "__main__":
    
    root = window.tk.Tk()
    app = window.Window(master=root)
    app.mainloop()

    print(os.path.dirname(__file__))
