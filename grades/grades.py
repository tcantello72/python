score = input('Please enter your score: ')
try:
    fscore = float(score)
    if fscore > 1:
        print('Great Score')
    elif fscore >= 0.9:
        print('A')
    elif fscore >= 0.8:
        print('B')
    elif fscore >= 0.7:
        print('C')
    elif fscore >= 0.6:
        print('D')
    elif fscore < 0.6:
        print('F')
except:
    print('Please enter a number for your score.')