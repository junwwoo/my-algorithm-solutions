numbers = [1,2,3,4,5,6]
newNumbers= []

for i in numbers:
    if(i%2 == 0):
        newNumbers.append(i**2)

print(newNumbers)

newNumbers2 = [num**2 for num in numbers if num %2 == 0]
print(newNumbers2)



