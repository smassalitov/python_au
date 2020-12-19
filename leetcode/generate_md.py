def get_name(all_lines):
    name = all_lines[0]
    name_list = list(name)
    name_list[0] = ''
    i = 1
    while name_list[i - 1] != '.':
        name_list[i - 1] = ''
        i += 1
    dot_place = name.find('.')
    name_list[dot_place] = ''
    name.strip()
    name = ''.join(name_list)
    name1 = "-".join(name.split())
    return [name, name1]


def get_url(all_lines):
    return all_lines[1]


def get_code(all_lines, fout):
    print('```python', file=fout)
    for i in range(2, len(all_lines)):
        print(all_lines[i], file=fout)
    print('```', file=fout)


def print_mark_down(all_lines, all_linked_lines, fout):
    for i in range(len(all_linked_lines)):
        if all_linked_lines[i] == '':
            all_linked_lines.insert(i, '+ [{}](#{})'.format(get_name(all_lines)[0], get_name(all_lines)[1]))
            break
    for i in all_linked_lines:
        print(i, file=fout)
    print('## ' + str(get_name(all_lines)[0]), file=fout)
    print(get_url(all_lines), file=fout)
    get_code(all_lines, fout)


def main():
    with open("source_leetcode_data.txt", 'r') as fin:
        all_lines = fin.read().splitlines()
    with open('test_out.md', 'r') as fin:
        all_linked_lines = fin.read().splitlines()
    fout = open("test_out.md", "w")
    print_mark_down(all_lines, all_linked_lines, fout)

if __name__ == "__main__":
    main()