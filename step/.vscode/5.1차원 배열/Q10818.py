# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

user_input=int(input())
array_number=list(map(int,input().split()))
print(min(array_number), max(array_number))
