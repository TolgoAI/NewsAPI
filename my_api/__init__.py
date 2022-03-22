'''Building an app that acquires data from an API and loads data to CSV file. NewsAPI is taken as an example'''

import requests
url = "https://newsapi.org/v2/everything?q=ukraine&war&language=en&sortBy=publishedAt&apiKey=YOUR_API_KEY"

def get_data():
    try:
        response = requests.get(url, timeout = 3)
        response.raise_for_status()
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:",errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt)
    else:
        return response.json()

data = get_data()
print(data)

# WRITE DATA INTO A FILE 

# create a file and open it in writing mode with the following fields
f = open("ukraine_war.csv", "w")
print("source_id\001source_name\001author\001title\001description\001url\001url_to_image\001published_at\001content", file = f)

# defines a function that gathers data and writes them in a new file
def expected_output():
    for article in data["articles"]:
        source_id = article["source"]["id"]
        source_name = article["source"]["name"]
        author = article["author"]
        title  = article["title"]
        description = article["description"]
        url = article["url"]
        url_to_image = article["urlToImage"]
        published_at = article["publishedAt"]
        content = article["content"]
        # 001 is a bullet-proof delimiter
        output = f"{source_id}\001{source_name}\001{author}\001{title}\001{description}\001{url}\001{url_to_image}\001{published_at}\001{content}"
        print(output, file = f)
expected_output()
f.close()