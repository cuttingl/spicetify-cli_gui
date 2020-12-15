import subprocess
import os

     
def update_spotify():
    dirname = os.path.dirname(__file__)
    filename = dirname.__add__("/powershell_scripts/update_spotify.ps1")
    os.system(filename)

def update_css_spicetify():
    os.system("spicetify update")
    os.system("spicetify")

def install_spicetify():
    dirname = os.path.dirname(__file__)
    filename = dirname.__add__("/powershell_scripts/install_spicetify.ps1")
    os.system("Invoke-WebRequest -UseBasicParsing 'https://raw.githubusercontent.com/khanhas/spicetify-cli/master/install.ps1' | Invoke-Expression")

def test():
    dirname = os.path.dirname(__file__)
    filename = dirname.__add__("/powershell_scripts/test_script.ps1")
    os.system(filename)


if __name__ == "__main__":
    test()