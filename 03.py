# 파이썬 연습
# 접미사인지 확인하기
## 프로그래머스 0 레벨

def initList(my_string):
    suffix_list = []
    for idx in range(len(my_string)):
        suffix_list.append(my_string[idx:])
        
    return suffix_list

def solution(my_string, is_suffix):
    answer = 0
    suffix_list = initList(my_string)
    
    if is_suffix in suffix_list:
        answer = 1
    
    return answer