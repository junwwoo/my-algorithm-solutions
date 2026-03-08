# 2개를 동시에 순회하려면 zip()을 사용해야 됨

names = ['철수', '영희', '민수']
scores = [90, 85, 70]

myDict = {}

for name, score in zip(names, scores):
  myDict[name] = score

print(myDict)

# 1줄짜리 방법
# dict()는 파이썬 내장 함수
result = dict(zip(names, scores))
print(result)

# unpacking 활용 (result.items()을 써야 딕셔너리의 값까지 가져올 수 있음)
for name, score in result.items():
  print(f"{name}: {score}")