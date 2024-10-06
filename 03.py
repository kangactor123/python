# 파이썬 연습

# 접미사인지 확인하기
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

# 글자 이어 붙여 문자열 만들기
def solution(my_string, index_list):
    answer = ''
    for idx in index_list:
        answer += my_string[idx]
    return answer

# 수 조작하기 1
def solution(n, control):
    answer = n
    map = { "w": 1, "s": -1, "d": 10, "a": -10 }
    
    for char in control:
        answer += map[char]

    return answer