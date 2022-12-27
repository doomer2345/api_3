import os
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv
import argparse


def shorten_link(api_key, user_url):

    headers = {
        'Authorization': f'Bearer {api_key}'
    }

    payload = {
        "long_url": user_url
    }

    url = 'https://api-ssl.bitly.com/v4/shorten'
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()["link"]


def count_clicks(api_key, user_url):

    headers = {
        'Authorization': f'Bearer {api_key}'
    }

    url = f'https://api-ssl.bitly.com/v4/bitlinks/{user_url}/clicks/summary'
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()["total_clicks"]


def is_bitlink(user_url):
    headers = {
        'Authorization': f'Bearer {api_key}'
    }

    url = f'https://api-ssl.bitly.com/v4/bitlinks/{user_url}'
    response = requests.get(url, headers=headers)
    return response.ok


if __name__ == "__main__":
    load_dotenv()
    api_key = os.environ['BITLY_APIKEY']
    parser = argparse.ArgumentParser(
        description='программа сокращает ссылки и считает клики '
    )
    parser.add_argument('link', help='Ваша ссылка')
    args = parser.parse_args()
    parsed_url = urlparse(args.link)
    url_without_scheme = f"{parsed_url.netloc}{parsed_url.path}"

    
    try:
        if is_bitlink(args.link):
            print('Количество кликов', count_clicks(api_key, url_without_scheme))
        else:
            print('Битлинк', shorten_link(api_key, args.link))
    except requests.exceptions.HTTPError:
        print("Ошибка при запросе.Вы ввели неверную ссылку или неверный токен")
