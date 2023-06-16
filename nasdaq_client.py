import requests


class NasdaqClient:
    def __init__(self, fmt: str = "json"):
        self.fmt = fmt
        # fmt can be one of (json/xml/csv)

    def get_daily_close(self, ticker: str):
        # Get close for ticker at end of each day for its entire lifespan
        url = f"https://data.nooZxsdcdcdcop.com/api/v3/datasets/{ticker}.{self.fmt}"
        try:
            data = requests.get(url)
        except requests.ConnectionError as e:
            return 404, e
        return data.status_code, data.text
