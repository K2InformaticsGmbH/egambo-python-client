from egambo import tcpjson
import json
import argparse


class Client:

    def __init__(self, host, port):
        self.tj = tcpjson.TcpJson(host, port, True)
    
    def login(self, username, password):
        message = {"action": "login", "user": username, "password": password}
        self.tj.send(message)
        resp = self.tj.recv()
        if resp["resp"] and resp["resp"] == "ok":
            return "ok"
        return resp

    def new_game(self):
        message =  {"action": "new_game", "type": "tic_tac_toe", "opponent": 1}
        self.tj.send(message)
        resp = self.tj.recv()
        if resp["msg"]:
            print("resp : ", resp)
            resp2 = self.tj.recv()
            if resp2["resp"]["msg"] and resp2["resp"]["msg"] == "Game created":
                return resp["msg"]
        return resp

    def play(self, game_id, position):
        message = {"action": "play", "game_id": game_id, "position": position}
        result = self.tj.send(message)
        resp = self.tj.recv()
        resp2 = self.tj.recv()
        print(resp2)
        resp3 = self.tj.recv()
        print(resp3)
        return resp
        # TODO: error handling and verify game response, e.g. valid move or win or not


if __name__ == '__main__':

    # collect arguments
    parser = argparse.ArgumentParser(description='TicTacToe SSL wrapper')
    parser.add_argument('-ip', '--ip_address', default='127.0.0.1', help='server IP address (default 127.0.0.1)')
    parser.add_argument('-p', '--port', default=7443, type=int, help='server TCP/SSL port (default 7443)')
    parser.add_argument('-ns', '--no-ssl', action="store_true", help='server type TCP or SSL (default)')
    parser.add_argument('-un', '--username', default="peter", help='Player name')
    parser.add_argument('-pw', '--password', default="change_on_install", help='Player password')
    args = parser.parse_args()
    host = args.ip_address
    port = args.port

    # create and play the game
    client = Client(host, port, args.username, args.password)
    game_id = client.new_game()
    client.play(game_id, 2)
