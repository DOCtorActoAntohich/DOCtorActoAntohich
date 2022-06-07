# AoS2 hwB spam

This is a simple script that I used in training mode to continiously spam hwB for memory leak testing (not a great idea tho).

It demonsrates the usage of the following:
  - `keyboard` and `pyautogui` modules (very basic).
  - `threading` module:
    - Custom `Thread` via subclass.
    - `Semaphore` and some very basic one-way thread communication (parent to child).

Not tested on Windows ~~but should work. I hope. The whole humankind does.~~

### How to run

1. `sudo python3 -m pip install pyautogui keyboard`
2. `sudo python3 aos2_hwb_spam.py`
3. Follow the instructions the script shows.

For Windows, omit `sudo` completely.

However, `sudo` is a must for Linux because this baka [reads from some file that needs root access](https://pypi.org/project/keyboard/).

### How to adapt for other tasks

1. Change keys in the beginning (or inside `main` directly).
2. Edit `CustomScript::execute_custom_script` method.
