"""
find_cake_iter.py v1.00
"""
import requests

# GET 'Cake' page, 'text' property, in JSON format from Wikipedia API
api_response = requests.get('https://en.wikipedia.org/w/api.php?action=parse&section=0&prop=text&format=json&page=Cake', timeout=10)

# exit if response not '200 OK'
if api_response.status_code != 200:
    exit(print(f"Exiting - request non '200'\n{api_response}"))

# convert response to string
api_response = api_response.text

# initialise index position & counter to zero
startIndex = 0
count = 0

# iterate over api_response taking it's length as range
for i in range(len(api_response)):
    # search for string 'Cake' starting at position startIndex
    findCake = api_response.find('Cake', startIndex)

    # if cake is found:
    # - increase count by 1
    #  - continue search from next position

    if (findCake != -1):
        startIndex = findCake+1
        count += 1
        findCake = 0


print(f"\n'Cake' appears {count} times\n***Note*** Case Sensitive including corner cases e.g. 'Cakes'\n")
