# Q8. 숫자를 입력받아서 주어진 랜덤한 숫자가 맞는지 알아보는 코드 작성

import random

num_rand = random.randint(1, 100)

while(True):
    N = int(input())

    if (N > num_rand):
        print('입력한 수가 주어진 수보다 더 큼')
    elif (N < num_rand):
        print('입력한 수가 주어진 수보다 더 작음')
    else:
        print('정답~')
        break