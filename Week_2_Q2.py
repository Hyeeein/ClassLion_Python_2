# Q2. 첫 번째 줄에 입력 받은 두 자연수 A와 B를 사칙연산하는 코드 작성 (덧셈, 뺄셈, 곱셈, 나눗셈, 몫, 나머지)

A, B = input().split()  # 입력받은 값을 공백을 기준으로 분리

A = int(A)
B = int(B)

print('덧셈은', A+B)
print('뺄셈은', A-B)
print('곱셈은', A*B)
print('나눗셈은', A/B)
print('몫은', A//B)
print('나머지는', A%B)
