# AlgoInterface

### Stream ingestion
Included docker-compose file serves the basis for feeding data into the system for processing. Utilizing a redis database with time-series (TSDB) capabilities this allows us to throw data at the system without worrying about getting the order right. Data can also be thrown at the database in parallel.

### TSDB organization
Data flowing into the time-series database needs to be tagged appropriately for processing. Data in the TSDB is organized by timestamps that are provided at the time that data is added or automatically based on the time of insertion. More importantly, data is organized by keys and then optionally by labels. Keys will dictate an associate sub-graph that data will be fed to. For a given key/sub-graph the data type is going to be fixed. This could be ticker data, text, and eventually things like images. Namespaces in redis keys will be used to break up things like different tickers for stock data.

### Useful links

- [Redis-py documentation](https://redis.readthedocs.io/en/stable/commands.html)
- [Redis time series documentation](https://redis.io/commands/?group=timeseries)
- [Example of using redis-py to interface with time series data](https://redis.readthedocs.io/en/stable/examples/timeseries_examples.html)

## Setup
1. Install Poetry `curl -sSL https://install.python-poetry.org | python3 -`
1. Set up Poetry Autocomlete `poetry completions bash >> ~/.bash_completion`
1. Create poetry environment `poetry install`
