# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

user_input=int(input())

for i in range(1,user_input+1):
    print("*"*i) # 문자열 x 스칼라는 문자열 반복