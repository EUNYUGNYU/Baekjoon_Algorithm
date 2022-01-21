#두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# try-except 를 추가해야 한다.
while True:
    try:
        A,B=map(int,input().split())
        print(A+B)
    except:
        break

# try-except가 밖에 오게 하기 
try:
    while True:
        A,B=map(int,input().split())
        print(A+B)
except:
    exit()
    