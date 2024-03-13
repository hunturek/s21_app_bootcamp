tatoo:str = input()
for i in range(2):
  tatoo = tatoo + input()

m:list = [0, 4, 5, 6, 8, 9, 10, 12, 14]
ex:str = 'true';

if len(tatoo) != 15:
  ex = 'error'
else:
  for i in range(15):
    if i in m and tatoo[i] != '*':
      ex = 'false'
    if i not in m and tatoo[i] == '*':
      ex = 'false'
print(ex)
