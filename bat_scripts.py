import subprocess
import os


     
def update_spotify():
    dirname = os.path.dirname(__file__)
    filename = dirname.__add__("/update_spotify.bat")
    os.system(filename)

def update_css_spicetify():
    dirname = os.path.dirname(__file__)
    filename = dirname.__add__("/update_css.bat")
    os.system(filename)
