fin = open("source_leetcode_data.txt")
fout = open("linked-list.md", "a+")
with open('source_leetcode_data.txt', 'r') as fin:
    all_lines = fin.read().splitlines()


name = all_lines[0]
name_list = list(name)
name_list[0] = ''
i = 1
while name_list[i-1] != '.':
    name_list[i-1] = ''
    i+=1
dot_place = name.find('.')
name_list[dot_place] = ''
name.strip()
name = ''.join(name_list)

print('##' + str(name), file = fout)
print(all_lines[1], file = fout)
print('```python', file = fout)
for i in range(2, len(all_lines)):
    print(all_lines[i], file = fout)
print('```', file = fout)
