import json
import requests

main = json.loads(requests.get("http://asj.dothome.co.kr/api/quiz/").text) #자료를 가져온 후 json으로 변환

q = main.get("quiz") #문제
h = main.get("hint") #첫번째 힌트
h2 = main.get("hint2") #두번째 힌트
a = main.get("answer") #정답
w = main.get("why") #해설
n = 0 

print(q) #문제 출력
while True:
    v = input() #사용자의 값
    n += 1
    if v == a:
        print("정답!!")
        print("해설: ", w)
        break
    else:
        print("땡!")
    if n == 5: #사용자가 5번안에 못 맞출시
        print(h)
    elif n == 10: #사용자가 10번안에 못 맞출시
        print(h2)
    elif n == 15: #사용자가 15번안에 못 맞출시
        print("못맞췄네요")
        print("정답: ", a)
        break
