# Import the TradeStation auth package
import ts.auth as a

"""This is an example script to show how to use this library"""

# Establish your client
ts_key = "Your Key Provided by Tradestation"
ts_secret = "Your Secret Provided by Tradestation"
call_back_domain = "http://localhost:3000"

client = a.easy_client(ts_key, ts_secret, call_back_domain)