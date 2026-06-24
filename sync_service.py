import threading
import time

from api.api_client import APIClient

from database.db import (
    get_pending_activities,
    get_pending_screenshots,
    mark_activity_synced,
    mark_screenshot_synced
)

from config.sync_manager import (
    update_last_sync
)


class SyncService:

    def __init__(self):

        self.api = APIClient()

        self.running = False

        self.thread = None

    def start(self):

        if self.thread and self.thread.is_alive():

            print(
                "Sync already running"
            )

            return

        self.running = True

        self.thread = threading.Thread(
            target=self.run,
            daemon=True
        )

        self.thread.start()

        print(
            "Sync Thread Created"
        )
    def run(self):

        print("Sync Service Started")

        while self.running:

            try:

                print("syncing...")

                self.sync_activities()

                self.sync_screenshots()

            except Exception as e:

                print(
                    "SYNC ERROR:",
                    e
                )

            time.sleep(30)

    def sync_activities(self):

        activities = (
            get_pending_activities()
        )

        for activity in activities:

            activity_id = activity[0]

            success = (
                self.api.upload_activity(
                    activity
                )
            )

            if success:

                mark_activity_synced(
                    activity_id
                )

                update_last_sync()

                print(
                    f"Activity {activity_id} Synced"
                )

    def sync_screenshots(self):

        screenshots = (
            get_pending_screenshots()
        )

        for screenshot in screenshots:

            screenshot_id = screenshot[0]

            success = (
                self.api.upload_screenshot(
                    screenshot
                )
            )

            if success:

                mark_screenshot_synced(
                    screenshot_id
                )

                update_last_sync()

                print(
                    f"Screenshot {screenshot_id} Synced"
                )

    def stop(self):

        self.running = False

        if self.thread:

            self.thread.join(
                timeout=1
            )

            self.thread = None