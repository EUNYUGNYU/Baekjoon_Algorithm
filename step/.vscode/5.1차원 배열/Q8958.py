""" "OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. 
O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 
문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다.
예를 들어, 10번 문제의 점수는 3이 된다.

"OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.

OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오."""



user_input=int(input())

for i in range(user_input):
    ox_array=list(input()) #리스트 넣어면 각 알파벳별로 엘티먼트가 구분됨
    score=0
    sum_score=0
    for ox in ox_array:
        if ox == 'O':
            score += 1
            sum_score += score
        else:
            score=0 # 이렇게 스탑
    print(sum_score)