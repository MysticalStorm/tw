import argparse
from server import app

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--ip', metavar='N', type=str)
parser.add_argument('--port', metavar='N', type=int)
args = parser.parse_args()
app.run(host=args.ip, port=args.port)