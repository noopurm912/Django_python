# def arraycheck(arr):
#
#     for i in range(len(arr)-2):
#         if arr[i] == 1 and arr[i+1] == 2 and arr[i+2] == 3:
#             return True
#         else:
#             return False
#
#
# a = arraycheck([1,2,4,4])
# print(a)


# def end_other(str1,str2):
#     str1 = str1.lower()
#     str2 = str2.lower()
#
#     if str1[-len(str2):] == str2:
#         return True
#     else:
#         return False
# we can also return str1.endswith(str2)
# f = end_other('abcxacb', 'xacb')
# print(f)
# def double_char(s):
#     res = ''
#     for i in s:
#         res += i*2
#     return res
# f = double_char('hello')
# print(f)


def get_guess():
    return list(input("what is your guess"))

x = get_guess()
print(type(x))
