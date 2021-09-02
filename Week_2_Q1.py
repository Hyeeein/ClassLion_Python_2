# Q1. 첫 번째 줄에 입력 받은 숫자 N에 따라, 첫 번째 줄부터 N 번째 줄까지 별을 출력하는 코드 작성

N = int(input())

for i in range(N):
    for j in range(i):
        print(' ', end = "")
    for j in range(N-i):
        print('*', end = "")
    print('')
