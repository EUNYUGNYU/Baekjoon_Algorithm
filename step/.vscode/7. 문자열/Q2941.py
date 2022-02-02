croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in croatia :
    word = word.replace(i, '*')  # word에 i가 있다면 *로 바꿔라
print(len(word)) # 문자열 str 개수 세기