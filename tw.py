import argparse
from server import app

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--ip', metavar='N', type=str)
parser.add_argument('--port', metavar='N', type=int)
parser.add_argument('--l', metavar='N', type=str)
parser.add_argument('--p', metavar='N', type=str)
args = parser.parse_args()

global login
global password
login=args.l
password=args.p

app.run(host=args.ip, port=args.port)