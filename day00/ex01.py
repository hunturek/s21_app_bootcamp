import argparse

parser = argparse.ArgumentParser(description='decypher')
parser.add_argument('string', type=str, help='decypher words')
args = parser.parse_args()
words:list = args.string.split(' ')

decypher:list = [word[0] for word in words]
print(decypher)
