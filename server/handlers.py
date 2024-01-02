import tornado.web
from rules import connectRule

# 连接处理
class ConnectHandler(tornado.web.RequestHandler):
    def post(self):
        user_name = self.get_argument("user_name")
        password = self.get_argument("password")
        user_info = {
            "user_name": user_name,
            "password": password
        }
        if not self.checkUser(user_info):
            self.write("<h1>YOU ARE NOT WELCOME!<h1>")
            self.finish()
        else:
            client_ip = self.request.remote_ip
            res_data = {
                "local_ip": "127.0.0.1",
                "words": "HELLO {}, WELCOME TO DEEPSEA".format(user_name),
                "server_ip": client_ip
            }
            self.write(res_data)

    @connectRule
    def checkUser(self, info):
        user_name = info.get("user_name", "None")
        password = info.get("password", "None")
        if user_name != "niudewei":
            return
        return True