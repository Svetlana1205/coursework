
import requests
import configparser
import json
from tqdm import tqdm
from pprint import pprint

config = configparser.ConfigParser()
config.read('settings.ini')
access_token = config['Tokens']['vk_token']
user_id = config['Id']['user_id']
ya_token = config['Tokens']['ya_token']

# print(access_token)
# print(user_id)

class VK:
    def __init__(self, access_token,  version='5.199'):
        self.base_url = 'https://api.vk.com/method/'
        self.params = {
            'access_token': access_token,
            'v': version
        }

    def get_user_photos(self, user_id, count=10):
        url = f'{self.base_url}photos.get'
        params = {'owner_id': user_id, 'album_id': 'profile', 'count': count, 'extended': '1'}
        params.update(self.params)
        response = requests.get(url, params=params)
        photos = response.json()['response']['items']
        return photos

        result = []

        

vk_instance = VK(access_token)

# Вызов метода через экземпляр
photos_response = vk_instance.get_user_photos(user_id)
pprint(photos_response)