user_file = input('Enter file name: ')
if len(user_file) < 1:
    user_file = 'mbox-short.txt'
file_handler = open(user_file)
hour = dict()
results = list()
for line in file_handler:
    line = line.rstrip()
    if not line.startswith('From '): 
        continue
    words = line.split()
    colon = words[5].find(':')
    hr = words[5][:colon]
    if hr not in hour:
        hour[hr] = 1
    else:
        hour[hr] += 1
for (hr_key, count) in list(hour.items()):
    results.append((hr_key, count))
results.sort()
for (hr_key, count) in results:
    print(hr_key, count)