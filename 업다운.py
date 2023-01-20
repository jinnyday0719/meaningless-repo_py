from random import randint

rn = randint(1, 101) #1부터 100까지 랜덤한수 추출

print("업다운 시작!")

while True:
    try:
        n = int(input()) #이용자의 값 받기
        if n < rn:
            print("up!")
        elif n > rn:
            print("down!")
        else:
            print("정답!!")
            break
    except:
        print("숫자만 입력해 주세요!")
