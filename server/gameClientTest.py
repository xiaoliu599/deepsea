import tornado.httpclient

class GameClient():
    def __init__(self):
        self.client = tornado.httpclient.HTTPClient()

    def Connect(self):
        user_info = {
            "user_name": "niudewei",
            "password": "123456"
        }
        response = self.client.fetch("http://127.0.0.1:8000/connect", method = "POST")
        if not response:
            return
        print("GET FROM SERVER:", response.body.decode())
        serv_data = response.body.decode()
        return serv_data

if __name__ == '__main__':
    game_client = GameClient()
    game_client.Connect()