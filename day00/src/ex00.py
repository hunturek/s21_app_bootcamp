import argparse

parser = argparse.ArgumentParser(description='blockchain')
parser.add_argument('str_count', type=str, help='Count of blockchain strs')
args = parser.parse_args()

result_list: list = []

for i in range(int(args.str_count)):
    inp_str: str = input()
    if inp_str[:5] == '00000' and len(inp_str) == 32 and inp_str[5] != '0':
        result_list.append(inp_str)

for result in result_list:
    print(result)
