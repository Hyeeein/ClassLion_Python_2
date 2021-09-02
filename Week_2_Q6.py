# Q6. 첫 번째 줄에 자연수 N을 입력 받고, 두 번째 줄에 N개에 정수를 공백으로 구분해서 입력받은 후에 최솟값과 최댓값을 구하는 코드 작성

N = int(input())
data = list(map(int, input().split())) # 입력받은 여러 개의 데이터를 list로 변환

print('최솟값은', min(data), ', 최댓값은', max(data))