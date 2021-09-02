# Q3. 첫 번째 줄에 입력 받은 두 정수 A와 B를 비교하는 코드 작성 (A를 기준으로 비교)

A, B = input().split()  # 입력받은 값을 공백을 기준으로 분리

A = int(A)
B = int(B)

if (A > B):
    print(A, '>', B)
elif (A < B):
    print(A, '<', B)
else:
    print(A, '=', B)