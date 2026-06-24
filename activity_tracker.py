from pynput import mouse
from pynput import keyboard


class ActivityTracker:

    def __init__(self):

        self.mouse_count = 0
        self.keyboard_count = 0

        self.mouse_listener = None
        self.keyboard_listener = None

    # for mouse events
    def on_move(self, x, y):

        self.mouse_count += 1


    #for keyboard events
    def on_press(self, key):

        self.keyboard_count += 1
    
    #start from here 
    def start(self):

        self.mouse_listener = mouse.Listener(
            on_move=self.on_move
        )

        self.keyboard_listener = keyboard.Listener(
            on_press=self.on_press
        )

        self.mouse_listener.start()
        self.keyboard_listener.start()
    
    #stop from here
    def stop(self):

        if self.mouse_listener:
            self.mouse_listener.stop()

        if self.keyboard_listener:
            self.keyboard_listener.stop()

    def get_counts(self):

        return (
            self.keyboard_count,
            self.mouse_count
        )
    
    def reset_counts(self):

        self.keyboard_count = 0
        self.mouse_count = 0