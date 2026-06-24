import time

from tracking.activity_tracker import (
    ActivityTracker
)

tracker = ActivityTracker()

tracker.start()

print("Tracking Started")

time.sleep(15)

keyboard_count, mouse_count = (
    tracker.get_counts()
)

print(
    "Keyboard:",
    keyboard_count
)

print(
    "Mouse:",
    mouse_count
)

tracker.stop()