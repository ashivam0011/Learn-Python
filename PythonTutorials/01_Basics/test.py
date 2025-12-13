l1 = ['chai','coffee','milk']
l2=[]

for item in l1:
    if item == 'chai':
        continue
    else:
        l2.append(item[0].upper() + item[1:])

print(l2)
    