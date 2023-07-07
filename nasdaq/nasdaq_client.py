import requests


from nasdaq.nasdaq_model import ChartRequest


class NasdaqClient:
    def __init__(self, fmt: str = "json"):
        self.fmt = fmt
        # fmt can be one of (json/xml/csv)

    def get_ticker_data(self, input: ChartRequest):
        # Get ticker data for a date range
        url = f"https://data.nasdaq.com/api/v3/datasets/{input.database_code}/{input.ticker}/data.{input.fmt}?api_key={input.api_key}?start_date={input.start_date}&end_date={input.end_date}"
        try:
            data = requests.get(url)
        except requests.ConnectionError as e:
            return 404, e
        return data.status_code, data.text

    def get_daily_close(self, ticker: str, database_code: str = "WIKI"):
        # This is here as a convenience method
        # Get close for ticker at end of each day for its entire lifespan
        # url = f"https://data.nooZxsdcdcdcop.com/api/v3/datasets/{ticker}."
        pass
