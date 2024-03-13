import sys

for i in sys.argv[0]:
  new_string:str = input()
  if new_string[:5] == "00000" and len(new_string) == 32:
    print(new_string)
