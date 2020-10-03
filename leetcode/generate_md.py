with open("source_leetcode_data.txt", 'r') as fin:
    all_lines = fin.read().splitlines()
with open('linked-list.md', 'r') as fin:
    all_linked_lines = fin.read().splitlines()
fout = open("linked-list.md", "w")


def GetName(all_lines):
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
    name1 =  "-".join(name.split())
    return [name, name1]


def GetUrl(all_lines):
    return all_lines[1]


def GetCode(all_lines):
    print('```python', file=fout)
    for i in range(2, len(all_lines)):
        print(all_lines[i], file=fout)
    print('```', file=fout)
    
    
def PrintMarkDown(all_lines):
    for i in range(len(all_linked_lines)):
        if all_linked_lines[i] == '':
            all_linked_lines.insert(i, '+ [{}](#{})'.format(GetName(all_lines)[0], GetName(all_lines)[1]))
            break
    for i in all_linked_lines:
        print(i, file=fout)
    print('## ' + str(GetName(all_lines)[0]), file = fout)
    print(GetUrl(all_lines), file = fout)
    GetCode(all_lines)
PrintMarkDown(all_lines)
