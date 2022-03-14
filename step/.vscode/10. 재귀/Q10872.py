"""0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오."""

# 1. 나의 답: for 문으로 풀기
num=int(input())

x=1
for i in range(1,num+1):
    x=x*i
print(x)


# 2. 재귀로 풀기

def factorial(n):
    result = 1
    if n > 0 :
        result = n * factorial(n-1)
    return result

n = int(input())
print(factorial(n))