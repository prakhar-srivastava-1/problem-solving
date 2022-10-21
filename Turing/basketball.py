ops = ['5', '2', 'C', 'D', '+']
results = []


for each in ops:
    if each.isdigit():
        print('int')
        results.append(int(each))
    
    elif each == 'C':
        results.pop()

    elif each == 'D':
        results.append(results[-1] * 2)

    elif each == '+':
        results.append(results[-1] + results[-2])

print(sum(results))