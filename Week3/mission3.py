listA = [1, 5, 2, 3]
listB = [2, 3, 4, 5, 9]

newList = set(listA).intersection(listB)
print(newList)

# 리스트에는 교집합 메소드가 없기 때문에 set으로 변환한 뒤에 사용해야 됨

# & 연산자를 사용해도 동일하게 동작함

newList2 = set(listA) & set(listB)
print(newList2)
