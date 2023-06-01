number = 0
while True:
    input_value = input('Please enter a number or Done when finished: ')
    if input_value == 'done':
        break
    try:
        value = int(input_value)        
    except:
        print('Invalid input')
        continue
    if number == 0:
        smallest = value
        largest = value
    elif value < smallest:
        smallest = value
    elif value > largest:
        largest = value    
    number = number + 1
print('Maximum is',largest)
print('Minimum is',smallest)