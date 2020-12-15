import subprocess
import os
import sys

     
def update_spotify():
    dirname = os.path.dirname(__file__)
    filename = dirname.__add__("/powershell_scripts/update_spotify.ps1")
    p = subprocess.Popen(["powershell.exe",filename], stdout=sys.stdout)
    p.communicate()

def update_css():
    dirname = os.path.dirname(__file__)
    filename = dirname.__add__("/powershell_scripts/update_css.ps1")
    p = subprocess.Popen(["powershell.exe",filename], stdout=sys.stdout)
    p.communicate()

def install_spicetify():
    dirname = os.path.dirname(__file__)
    filename = dirname.__add__("/powershell_scripts/install_spicetify.ps1")
    p = subprocess.Popen(["powershell.exe",filename], stdout=sys.stdout)
    p.communicate()

def test():
    dirname = os.path.dirname(__file__)
    filename = dirname.__add__("/powershell_scripts/test_script.ps1")
    p = subprocess.Popen(["powershell.exe",filename], stdout=sys.stdout)
    p.communicate()

def launch_script(script_name):
    dirname = os.path.dirname(__file__)
    filename = dirname.__add__("/powershell_scripts/" + script_name)
    p = subprocess.Popen(["powershell.exe",filename], stdout=sys.stdout)
    p.communicate()