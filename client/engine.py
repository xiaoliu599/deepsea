import requests
import asyncio

class GameEngine():
    def __init__(self):
        pass

    def menu(self):
        while True:
            print("============  deepsea  ============ \n")
            print("\n")
            print("        1.login\n")
            print("        2.logout\n")
            print("===================================")
            door_num = input("input menu number: ")
            if door_num == "1":
                self.login()
                break
            elif door_num == "2":
                self.logout()
                break
            else:
                print("please input menu number")


    def login(self):
        user_name = input("input your user name: ")
        password = input("input your password: ")
        user_info = {
            "user_name": user_name,
            "password": password
        }
        res = requests.post(url = "http://127.0.0.1:8000/connect", params = user_info)
        print(res.text)


    def logout(self):
        pass

    def startGame(self):
        self.menu()

if __name__ == '__main__':
    engine = GameEngine()
    engine.startGame()

