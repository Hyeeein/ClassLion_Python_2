# Q4. 첫 번째 줄에 입력 받은 자연수 N에 따라서 구구단 N단을 출력하는 코드 작성

N = int(input())  # 자연수 N 입력 받음

for i in range(1, 10):
    print(N, '*', i, '=', N*i)