import threading
import time

from tracking.screenshot import take_screenshot

from tracking.activity_tracker import (
        ActivityTracker
    )
from tracking.activity_logger import (
        ActivityLogger
    )

from tracking.sync_service import (
    SyncService
)
from database.db import create_session
from database.db import (
    create_session,
    stop_session
)


class Tracker:

    def __init__(self):

        self.is_tracking = False
        self.thread = None

        self.activity_tracker = (
        ActivityTracker()
        )

        self.activity_logger = (
            ActivityLogger(
                self.activity_tracker,
                self
            )
        )

        self.sync_service = (
            SyncService()
        )

        self.session_id = None
        

    def start_tracking(self):

        if self.is_tracking:
            return

        self.is_tracking = True

        self.session_id = create_session()
        print(
            "Created Session:",
            self.session_id
        )

        self.activity_tracker.start()

        self.activity_logger.start()

        self.sync_service.start()

        self.thread = threading.Thread(
            target=self.run_tracking,
            daemon=True
        )

        self.thread.start()

       

    def run_tracking(self):

        while self.is_tracking:

            take_screenshot()

            time.sleep(60)

    def stop_tracking(self):
        print(
            "Tracker Stop Called"
        )

       
        self.is_tracking = False

        self.activity_tracker.stop()

        self.activity_logger.stop()

        self.sync_service.stop()

        if self.session_id:

            stop_session(
                self.session_id
            )

            print(
                f"Session {self.session_id} Closed"
            )



       