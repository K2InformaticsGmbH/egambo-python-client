from egambo import tcpjson
import json
import argparse


class TicTacToeSSL:

    def __init__(self, host, port):
        self.tj = tcpjson.TcpJson(host, port, True)
        self.game_id = ""

    def login(self, player, password):
        message = {"action": "login", "user": player, "password": password}
        result = self._send_and_receive(message)
        # TODO: error handling, e.g. check if response is OK.

    def new_game(self):
        message =  {"action": "new_game", "type": "tic_tac_toe", "opponent": 1}
        result = self._send_and_receive(message)
        print(result)

    def play(self, position):
        message = {"action": "play", "game_id": self.game_id, "position": position}
        result = self._send_and_receive(message)
        # TODO: error handling and verify game response, e.g. valid move or win or not

    def _send_and_receive(self, message):
        result = self.tj.send(message)
        return result


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
    game = TicTacToeSSL(host, port)
    game.login(args.username, args.password)
    game.new_game()
    game.play(2)
