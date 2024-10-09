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

# 마지막 두 원소
import copy

def solution(num_list):
    answer = copy.deepcopy(num_list)
    n1, n2 = answer[-1], answer[-2]
    num = 0
    
    if n1 > n2:
        num = n1 - n2
    else:
        num = n1 * 2
        
    answer.append(num)
    return answer

# 원소들의 곱과 합
def solution(num_list):
    num_sum = 0
    num_multiple = 1
    
    for num in num_list:
        num_sum += num
        num_multiple *= num
        
    return int(num_sum ** 2 > num_multiple)

# 두 수의 연산값 비교하기
# 나의 풀이
def solution(a, b):
    answer = 0
    num1, num2 = int(str(a) + str(b)), 2 * a * b
    
    if num1 >= num2:
        answer = num1
    else:
        answer = num2
        
    return answer
# python method를 활용한 풀이
# max 메서드를 활용하면 쉽게 숫자를 비교해 리턴받을 수 있음
def solution(a, b):
    return max(int(f"{a}{b}"), 2 * a * b)

# 카운트 업
# 나의 풀이
def solution(start_num, end_num):
    answer = []

    while start_num <= end_num:
        answer.append(start_num)
        start_num += 1
        
    return answer

# python method를 활용한 풀이
# list 메서드와 range 메서드를 사용하면 쉽게 list를 만들 수 있음
def solution(start, end):     
    return list(range(start, end + 1))

# 조건에 맞게 수열 변환하기 3
def isOdd(num):
    return num % 2 == 1

# python 삼항 연산자 사용법
# 값1 if 조건 else 값2
def solution(arr, k):
    answer = []
    for num in arr:
        calNum = num * k if isOdd(k) else num + k
        answer.append(calNum)
        
    return answer

# 홀수 vs 짝수
# 나의 풀이
def solution(num_list):
    sum_even, sum_odd = 0, 0
    for idx in range(len(num_list)):
        if idx % 2 == 0:
            sum_even += num_list[idx]
        else: 
            sum_odd += num_list[idx]
        
    return sum_even if sum_even >= sum_odd else sum_odd

# python 슬라이싱 활용
def solution(num_list):
    return max(sum(num_list[::2]), sum(num_list[1::2]))

# 0 떼기
# 나의 풀이
def solution(n_str):
    flag = False
    
    str_list = list(n_str)
    
    for idx in range(len(str_list)):
        if str_list[idx] != "0":
            flag = True
        
        if flag:
            str_list = str_list[idx::]
            break

    return "".join(str_list)

# python method 활용
# strip lstrip rstrip: 문자열에서 특정 문자(인자가 없을 경우 공백)를 제거한다
def solution(str):
    return str.lstrip("0")

# 배열의 길이에 따라 다른 연산하기
def solution(arr, n):
    length = len(arr)
    
    # 원소의 갯수가 홀수 일 경우 (1 = True)
    if length % 2:
        for idx in range(0, length, 2): arr[idx] += n
    # 원소의 갯수가 짝수 일 경우
    else:
        for idx in range(1, length, 2): arr[idx] += n
        
    return arr