import requests


def send_payload(target_url):
    response = requests.get(target_url)
    return response.text
