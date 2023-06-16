"""
Not in love with the name, but this file will be a template for feeding data into the TSDB. Maybe we can have a class here that will be inherited to stuff different data in for ingestion.
"""


import redis

r = redis.Redis()
ts = r.ts()

# Create a timeseries
ts.create("ticker_data:APPL")

ts.add("ticker_data:APPL", 1657265437756, 124.3)



ts.create("financial_data:AMD")

ts.add("financial_data:AMD", 1657265437750, "Lots of html or something that was scraped")