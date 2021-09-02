# Q5. 두 정수 A와 B를 여러 줄에 걸쳐 입력 받은 다음 A+B를 출력하는 코드 작성

while (True):
    A, B = map(int, input().split())    # map(적용시킬 함수, 적용할 값들)

    print(A, '+', B, '=', A+B)
