#두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

user_input=int(input())

for i in range(1,user_input+1):
    A,B=map(int,input().split())
    print("Case #"+str(i)+":",A,"+",B,"=",A+B) #,와는 달리 +는 기본 띄어쓰기 x