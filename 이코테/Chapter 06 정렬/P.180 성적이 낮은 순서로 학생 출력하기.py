""" P.180 성적이 낮은 순서로 학생 출력하기 """

""" 내 풀이 """
n = int(input())
array = []
for _ in range(n):
    name, score = input().split()
    array.append((name, int(score)))

array = sorted(array, key=lambda score: score[1])

for x in array:
    print(x[0], end=' ')
