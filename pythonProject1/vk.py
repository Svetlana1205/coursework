import requests

class VK:

    def __init__(self, access_token, user_id, version='5.131'):
        self.token = access_token
        self.id = user_id
        self.version = version
        self.params = {'access_token': self.token,'v': self.version}


    def users_info(self):
        url = 'https://api.vk.com/method/users.get'
        params = {'user_ids': self.id}
        response = requests.get(url, params={**self.params, **params})
        return response.json()


access_token = 'vk1.a.JAARBNyRXgNs0gpVgyQVgEhXzx5G0yQpT-wvQJn-dVsomHx23Zj7cS0EhP3KRQDHLNninWeCD6w8ID1Ud-65aCCKZbb7uFsgNEQj9QIuXb6TfT5r7Ve5Q_jz_L7ZoWXVru0vur-l-yD7LJMUuJO3GMwWV8QH40WZMwnVyBrSpySGt6euQy1d20JkwxxTtM_s' # токен полученный из инструкции
user_id = '72420187' # идентификатор пользователя vk
vk = VK(access_token, user_id)
print(vk.users_info())
