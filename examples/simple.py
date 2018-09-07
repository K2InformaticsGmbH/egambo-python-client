import argparse
import getpass
import egambo.tcpjson 


def main():
    parser = argparse.ArgumentParser(description='Interactive tic-tac-toe using egambo API client')
    parser.add_argument(
            '-ip', '--ip_address', default='127.0.0.1',
            help='server IP address (default 127.0.0.1)')
    parser.add_argument(
            '-p', '--port', default=7443, type=int,
            help='server TCP/SSL port (default 7443)')
    
    args = parser.parse_args()
    host = args.ip_address
    port = args.port

if __name__ == '__main__':
    main()