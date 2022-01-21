#두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.
A,B=map(int,input().split())

if A>B:
    print(">")
elif A<B:
    print("<")
else:
    print("==")    
    

#삼항 연산자 사용
#조건식 1이 참일 때 값 if 조건식 1 else [ 조건식2가 참일 때 값 if 조건식2 else 조건식이 모두 거짓일 때 값 ]
print('>') if A > B else print('<') if A < B else print('==')

