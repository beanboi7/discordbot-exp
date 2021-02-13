import json
import requests
def get_quote():
    response = requests.get("https://www.tronalddump.io/random/quote")
    json_data = json.loads(response.text) #gives us py dictonaries
    quote = json_data["value"]
    quote = quote + "\n" + "-Trump mama"
    return quote
