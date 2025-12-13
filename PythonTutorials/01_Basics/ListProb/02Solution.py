l1 = [1,2,3,4,5,6]


ans =0 

for x in l1:
    if x % 2 == 0:
        ans += x
    else:
        continue

print('Your final ans is: ',ans)