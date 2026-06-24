import threading
import time

from database.db import save_activity_log


class ActivityLogger:

    def __init__(
        self,
        activity_tracker,
        tracker
    ):

        self.activity_tracker = (
            activity_tracker
        )

        self.is_running = False

        self.thread = None

        self.tracker = tracker

    # start activity saver in DB
    def start(self):

        if self.is_running:
            return

        self.is_running = True

        self.thread = threading.Thread(
            target=self.run,
            daemon=True
        )

        self.thread.start()

    def run(self):

        while self.is_running:

            time.sleep(60)

            (
                keyboard_count,
                mouse_count
            ) = self.activity_tracker.get_counts()

            save_activity_log(
                self.tracker.session_id,
                keyboard_count,
                mouse_count,
            )

            print(
                f"Saved -> "
                f"K:{keyboard_count} "
                f"M:{mouse_count}"
            )

            self.activity_tracker.reset_counts()

    # stop activity saver in DB
    def stop(self):

        self.is_running = False