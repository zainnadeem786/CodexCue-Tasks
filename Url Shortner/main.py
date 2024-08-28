import requests

url = input('Enter The URL:')

def shorten_url(url):
    api_url = f"http://tinyurl.com/api-create.php?url={url}"
    response = requests.get(api_url)
    short_url = response.text
    print(short_url)

shorten_url(url)