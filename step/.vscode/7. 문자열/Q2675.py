"""문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오. 
즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. 
S에는 QR Code "alphanumeric" 문자만 들어있다.

QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다."""




user_input= int(input())

for i in range(user_input):
    num, s = input().split()
    text = '' # 빈문자열
    for i in s: # str을 리스트로 할 경우 알파벳 하나씩 쪼개짐
        text += int(num) * i #i는 문자열
    print(text)
