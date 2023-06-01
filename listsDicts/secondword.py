count = 0
file_handler = open('mbox-short.txt')
for line in file_handler:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    print(words[1])
    count = count + 1
print('There were',count,'lines in the file with From as the first word')