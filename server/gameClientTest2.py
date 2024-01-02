import requests

class GameClient():
    def connect(self):
        user_info = {
            "user_name": "niudewe",
            "password": "123456"
        }
        response = requests.post(url = "http://127.0.0.1:8000/connect", params = user_info)
        print(response.text)

if __name__ == '__main__':
    client = GameClient()
    client.connect()