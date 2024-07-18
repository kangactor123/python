var = 1
# print(var)
var += 3
# print(var)

list = [1,3,5]
list2 = [2, 5, 7]
list3 = list + list2

stringList = ["str", "str2"]
# print(list + stringList)
stringList.append(list2)
# print(stringList)

# slicing
# print(list3, list3[1:3], list3[:5:2])
# print("list3.len: ", len(list3))

if len(list3) == 6:
    print(len(list3), "입니다.")
elif len(list3) < 6:
    print("6 이하")
elif len(list3) > 6:
    print("6 이상")
else:
    print("else")

# for li in list3:
#     print(li)

for num in range(5):
    print(num)