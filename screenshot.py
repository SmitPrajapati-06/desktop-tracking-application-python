import pyautogui
from datetime import datetime

from database.db import save_screenshot

def take_screenshot():

    timestamp = datetime.now().strftime(
        "%Y-%m-%d_%H-%M-%S"
    )

    filename = f"{timestamp}.png"

    filepath = f"screenshots/{filename}"

    screenshot = pyautogui.screenshot()

    screenshot.save(filepath)

    save_screenshot(
        filename,
        filepath
    )

    print("Saved:", filename)

    return filename, filepath