file_name = ('romeo.txt')
file_handler = open(file_name)
results = list()
for line in file_handler:
    line = line.rstrip()
    words = line.split()
    for word in words:
        if word not in results:
            results.append(word)
results.sort()
print(results)