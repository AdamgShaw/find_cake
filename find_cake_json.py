"""
find_cake_json v1.00
"""
import requests
import re

# GET 'Cake' page, 'text' property, in JSON format from Wikipedia API
api_response = requests.get('https://en.wikipedia.org/w/api.php?action=parse&section=0&prop=text&format=json&page=Cake', timeout=10)

# exit if response not '200 OK'
if api_response.status_code != 200:
    exit(print(f"Exiting - request non '200'\n{api_response}"))

# compile regex pattern to match all html tags
remove_html = re.compile('<.*?>')

# convert api_response to dict
json_api_response = api_response.json()

# extract the value of the JSON key 'text'
json_text_value = (json_api_response["parse"]["text"]["*"])

# remove html tags, replace with single space
json_text_value = remove_html.sub(" ", json_text_value)

# create list of 'Cake' occurrences - case sensitive - no corner cases e.g 'Cakes'
find_cake = re.findall("\\bCake\\b", json_text_value)

# get length of list find_cake & print result
print(f"\n'Cake' appears {len(find_cake)} times - (case sensitive)\n")
