# spicetify-cli_gui

This is a project linked to [spicetify repository](https://github.com/khanhas/spicetify-cli).

---
## Installation :
Currently only available for Windows systems.
1. make sure you have the latest Python version
2. run :
```
pip3 install pyinstaller
```
3. add your "Scripts" folder to your PATH environment variable, should be at :
```txt
C:\Users\username\AppData\Local\Programs\Python\Python38\Scripts
```
4. run in your folder containing the project scripts :
```
pyinstaller --onefile -w main.py
```
5. Head to /dist folder
6. Enjoy the current (very simple) version !
___
## Objectives :
### 1. Provide a user friendly UI by preventing to write command lines to update Spotify's CSS like
```
spicetify update
```
```
spicetify backup apply
```
### 2. Available on any platform, any Linux systems
### 3. Not modifying config.ini file to select your theme
