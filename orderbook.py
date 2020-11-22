# Import libraries
import requests
import json
import csv

# Identifier for market code
market_code = "BTC-PLN"

# Function to get data from REST API based on market code identifier
# market_code - identifies for which pair data should be retrieved
def getTransactions(market_code):
    # URL for API to get orderbook lists
    url = "https://api.bitbay.net/rest/trading/orderbook/"+market_code
    # API headers
    headers = {'content-type': 'application/json'}
    # Return plain JSON message text
    return requests.request("GET", url, headers=headers).text

# Execute getTransaction function and store its output in response variable
response = getTransactions(market_code)
# Parse JSON message to navigate easily
parsed_response = json.loads(response)

# Open CSV file names "orderbook.csv"
with open(r'orderbook.csv', 'a', newline='') as csvfile:
    # Define field/column names accordingly with JSON message content
    fieldnames = ['type', 'ratio', 'current_amount', 'start_amount', 'past_amount', 'count_orders']
    # Create object to write CSV based on dictionary mapping
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    # Write header with prowided field/column names
    writer.writeheader()

    # For every entry in JSON message identified in "sell" section
    for entry in parsed_response["sell"]:
        # Write entry to CSV file as separate row (static type SELL)
        writer.writerow({'type': "SELL", 'ratio': entry["ra"], 'current_amount': entry["ca"], 'start_amount': entry["sa"], 'past_amount': entry["pa"], 'count_orders': entry["co"]})
        # Print entry to standard output
        print(entry)

    # For every entry in JSON message identified in "buy" section
    for entry in parsed_response["buy"]:
        # Write entry to CSV file as separate row (static type BUY)
        writer.writerow({'type': "BUY", 'ratio': entry["ra"], 'current_amount': entry["ca"], 'start_amount': entry["sa"], 'past_amount': entry["pa"], 'count_orders': entry["co"]})
        # Print entry to standard output
        print(entry)
