l1 = [1,2,3,4,5,-5,-10,-2]

print(l1)

count= 0

for item in l1:
    if item > 0:
        count += 1
print("Count of positive numbers:", count)