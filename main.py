# Import the TradeStation auth package
import ts.auth as a

"""This is an example script to show how to use this library"""

# Establish your client
ts_key = "Your Key Provided by Tradestation"
ts_secret = "Your Secret Provided by Tradestation"

client = a.easy_client(ts_key, ts_secret,"http://localhost:8080")