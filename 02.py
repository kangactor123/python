# 별만들기
for i in range(5):
    val = ''
    for j in range(5):
        if j != 5:
            val += '*'
    print(val)

# 역삼각형 만들기
num = 5
for i in reversed(range(num)):
    var = ''
    for j in range(i):
        var += '*'
    print(var)

# 삼각형 만들기
num = 10
output = ''
for i in range(1, num):
    for j in range(0, i):
        output += '*'
    output += '\n'

print(output)