from egambo import client
import json
import argparse

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
    cl = client.Client(host, port)
    "ok" == cl.login(args.username, args.password)
    game = cl.new_game()
    game_id = game["id"]
    cl.play(game_id, 2)
