
# Eye Blink Reminder Overlay

A lightweight, unobtrusive background utility built in Python. This program helps reduce eye strain during long screen sessions by displaying a transparent, animated overlay prompting you to blink 5 times per minute, evenly spaced out.

## Features

* **Transparent Overlay:** Uses a frameless, fully transparent window that sits on top of all other applications without interrupting your workflow.
* **Custom Animation:** Features a smooth, custom-drawn eye animation using Tkinter's Canvas.
* **Background Execution:** Runs entirely in the background without keeping a console or terminal window open.
* **Auto-Start:** Configured to launch automatically as soon as the PC boots up.

## Prerequisites

* **Python 3.x:** Ensure Python is installed and added to your system PATH.
* **Operating System:** Windows 11.

## Installation and Setup

1. **Clone or Download the Repository**
   Place `blinker.py` in a dedicated folder on your machine.

2. **Create the Execution Script**
   In the same folder, create a text file named `run_blinker.bat` and add the following line:
   ```bat
   start pythonw blink_overlay.py
    ``` 
   (Using pythonw instead of python ensures the script runs silently without opening a command prompt window.)

Enable Run on Startup

Press Win + R to open the Run dialog.

Type shell:startup and press Enter.

Right-click your run_blinker.bat file, copy it, and select Paste shortcut inside the Startup folder.

Usage
Once installed in the Startup folder, the program requires no manual intervention. It will start automatically when you log in.

The overlay will trigger immediately upon launch to confirm it is running.

It will appear in the center of your screen, execute a single blink, and hide itself again.

This process repeats automatically every 12 seconds (resulting in 5 blinks per minute).

To stop the program, open Windows Task Manager (Ctrl + Shift + Esc), find Python in the background processes, and select End task.

Customization
You can easily tweak the timing by modifying the variable in the __init__ method of blink_overlay.py:

self.interval_ms = 12_000 : Change how often the prompt appears (in milliseconds). The default is 12 seconds. For example, changing this to 60000 will make it appear only once a minute.


