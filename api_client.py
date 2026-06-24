import requests


class APIClient:

    BASE_URL = (
        "https://jsonplaceholder.typicode.com"
    )

    def upload_activity(
        self,
        activity
    ):

        try:

            response = requests.post(
                f"{self.BASE_URL}/posts",
                json={
                    "activity": str(activity)
                },
                timeout=5
            )

            return (
                response.status_code == 201
            )

        except Exception as e:

            print(
                "Activity Upload Error:",
                e
            )

            return False

    def upload_screenshot(
        self,
        screenshot
    ):

        try:

            response = requests.post(
                f"{self.BASE_URL}/posts",
                json={
                    "screenshot": str(
                        screenshot
                    )
                },
                timeout=5
            )

            return (
                response.status_code == 201
            )

        except Exception as e:

            print(
                "Screenshot Upload Error:",
                e
            )

            return False