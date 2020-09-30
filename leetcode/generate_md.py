fin = open("source_leetcode_data.txt")
fout = open("intervals.md", "a+")
with open('source_leetcode_data.txt', 'r') as fin:
    all_lines = fin.read().splitlines()
print('##' + all_lines[0], file = fout)
print(all_lines[1], file = fout)
print('```python', file = fout)
for i in range(2, len(all_lines)):
    print(all_lines[i], file = fout)
print('```', file = fout)
