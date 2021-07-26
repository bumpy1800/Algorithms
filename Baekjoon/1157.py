# 1157번 문제 : 단어 공부
# 주어진 단어에서 가장 많이 사용된 알파벳을 출력하는문제
# 중복일시 ?출력

word = input().upper() # 모두 대문자로 받기
words = list(set(word))  # 입력받은 문자열에서 중복값을 제거

count_list = []
for i in words : # count 숫자를 리스트에 넣는다
    count = word.count(i)
    count_list.append(count)  

if (count_list.count(max(count_list)) > 1) :  # count 숫자 최대값이 중복되어서 2이상이라면 ?를 출력
    print('?')
else:
    max_index = count_list.index(max(count_list))  # count 숫자 최대값 인덱스를 찾아서 출력해준다
    print(words[max_index])