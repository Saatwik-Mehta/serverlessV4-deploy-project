import requests



def sample_post(url):
    response = requests.post(url)
    return response.json()