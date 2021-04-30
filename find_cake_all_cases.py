"""
find_cake_all_cases.py v1.00
"""
import requests

# GET 'Cake' page, 'text' property, in JSON format from Wikipedia API
api_response = requests.get('https://en.wikipedia.org/w/api.php?action=parse&section=0&prop=text&format=json&page=Cake', timeout=10)

# exit if response not '200 OK'
if api_response.status_code != 200:
    exit(print(f"Exiting - request non '200'\n{api_response}"))

# convert response to string
api_response = api_response.text

# count & print 'Cake' occurrences - case-sensitive
print(f"'Cake' appears {api_response.count('Cake')} times - (case sensitive)")

# convert api_response to lowercase, count & print 'cake' occurrences - case-insensitive
print(f"'cake' appears {api_response.lower().count('cake')} times - (case insensitive)")
print("-" * 70,"\n**Note**\tAll results include corner cases e.g. 'cakes', 'cupcake' etc.")
