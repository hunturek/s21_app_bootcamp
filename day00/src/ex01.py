import argparse

parser = argparse.ArgumentParser(description='decipher')
parser.add_argument('cipher', type=str, help='String for decipher')
args = parser.parse_args()

result_list: list = args.cipher.split(' ')

for i in range(len(result_list)):
    result_list[i] = result_list[i][:1]

print(''.join(result_list))
