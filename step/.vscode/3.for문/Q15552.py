# 기존
user_input=int(input())

for i in range(user_input):
    a,b = map(int,input().split())
    print(a+b)
    
# 변경 (input-> sys)

import sys
user_input=int(sys.stdin.readline())

for i in range(user_input):
    a,b = map(int,sys.stdin.readline().split())
    print(a+b)