import time
import threading

import pyautogui
import keyboard


STOP_KEY = "]"
TOGGLE_KEY = "["


class KeyboardKey:
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__previous_state = None
        self.__current_state = False

    @property
    def name(self):
        return self.__name

    @property
    def previous_state(self):
        return self.__previous_state or False

    @property
    def current_state(self):
        return self.__current_state or False

    @property
    def is_held(self):
        return self.current_state

    @property
    def is_down(self):
        return self.current_state and not self.previous_state

    @property
    def is_up(self):
        return not self.current_state and self.previous_state

    def update(self):
        self.__previous_state = self.__current_state
        self.__current_state = keyboard.is_pressed(self.__name)


class CustomScript(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.__is_running = True
        self.__shall_execute_script = False
        self.__script_semaphore = threading.Semaphore()
        self.__running_semaphore = threading.Semaphore()

    @property
    def is_running(self):
        with self.__running_semaphore:
            return self.__is_running

    @property
    def shall_execute_script(self):
        with self.__script_semaphore:
            return self.__shall_execute_script

    def toggle_mode(self):
        with self.__script_semaphore:
            self.__shall_execute_script = not self.__shall_execute_script

    def stop(self):
        with self.__running_semaphore:
            self.__is_running = False

    def run(self):
        while self.is_running:
            if self.shall_execute_script: # ye im busy and im waitin...
                self.execute_custom_script()

    def execute_custom_script(self):
        pyautogui.keyDown("x")
        time.sleep(1 / 60 * 10)
        pyautogui.keyUp("x")

        time.sleep(1 / 60 * 30)


def main():
    print(f"`{TOGGLE_KEY}` to toggle execution (starts as disabled).")
    print(f"`{STOP_KEY}` or `Ctrl+C` to quit.")

    enabled = False
    stop_key = KeyboardKey(STOP_KEY)
    toggle_key = KeyboardKey(TOGGLE_KEY)

    custom_script_thread = CustomScript()
    custom_script_thread.start()

    try:
        while True:
            stop_key.update()
            if stop_key.is_down:
                break

            toggle_key.update()
            if toggle_key.is_down:
                custom_script_thread.toggle_mode()
                print(f"\nScript execution ", end="")
                print(("enabled" if enabled else "disabled."))
    except KeyboardInterrupt:
        pass
    finally:
        custom_script_thread.stop()
        print("\nFinishing last iteration of the script and stopping...")

    custom_script_thread.join()


if __name__ == "__main__":
    main()
