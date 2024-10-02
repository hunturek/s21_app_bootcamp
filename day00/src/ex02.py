result_str: str = ''
m_pos: list = [0, 4, 5, 6, 8, 9, 10, 12, 14]
result: bool = True

for i in range(3):
    inp_str: str = input()
    result_str = result_str + inp_str
    
for i in range(len(result_str)):
    if i in m_pos and result_str[i] != '*':
        result = False
    elif i not in m_pos and result_str[i] == '*':
        result = False
    
print(result)
