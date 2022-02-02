"""알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 
단, 대문자와 소문자를 구분하지 않는다."""


words = input().upper() # 대문자로 변환
unique_words = list(set(words))  # 입력받은 문자열에서 중복값을 제거

cnt_list = []
for i in unique_words : # 튜플이 들어감
    cnt = words.count(i) # 튜블에서 각 원소가 몇개인지 세기
    cnt_list.append(cnt)  # count 숫자를 리스트에 append

if cnt_list.count(max(cnt_list)) > 1 :  # count 숫자 최대값이 중복되면 (1개 이상 있다.)
    print('?')
else :
    max_index = cnt_list.index(max(cnt_list))  # count 숫자 최대값 인덱스(위치)
    print(unique_words[max_index])
