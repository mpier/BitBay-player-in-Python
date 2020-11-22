# Import libraries
import requests
import json
import csv

# Identifier for market code
market_code = "BTC-PLN"
# Identifier for quantity limit
limit = "100"

# Function to get data from REST API based on market code identifier
# market_code - identifies for which pair data should be retrieved
# query_params - list of parameters used for API call in concatenated string
def getTransactions(market_code, query_params):
    # URL for API to get recent transactions list
    url = "https://api.bitbay.net/rest/trading/transactions/"+market_code+"?"+query_params
    # API headers
    headers = {'content-type': 'application/json'}
    # Return plain JSON message text
    return requests.request("GET", url, headers=headers).text

# Execute getTransaction function (with provided parameters) and store its output in response variable
response = getTransactions(market_code, "limit="+limit)
# Parse JSON message to navigate easily
parsed_response = json.loads(response)

# Open CSV file names "last_transactions.csv"
with open(r'last_transactions.csv', 'a', newline='') as csvfile:
    # Define field/column names accordingly with JSON message content
    fieldnames = ['id', 'time', 'amount', 'rate', 'type']
    # Create object to write CSV based on dictionary mapping
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # For every entry in JSON message identified in "items" section
    for entry in parsed_response["items"]:
        # Write entry to CSV file as separate row
        writer.writerow({'id': entry["id"], 'time': entry["t"], 'amount': entry["a"], 'rate': entry["r"], 'type': entry["ty"]})
        # Print entry to standard output
        print(entry)
