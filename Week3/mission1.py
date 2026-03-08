numbers = [1,2,3,4,5,6]
newNumbers= []

for i in numbers:
    if(i%2 == 0):
        newNumbers.append(i**2)

print(newNumbers)

# 리스트 컴프리헨션 사용 코드
newNumbers2 = [num**2 for num in numbers if num %2 == 0]

print(newNumbers2)