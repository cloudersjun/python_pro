# coding:utf-8
# 汽水瓶问题
# str=raw_input()
# a = int(str)
# sum = int(0)
# if a != 0:
#     m = int(a / 3)
#     while m > 0:
#         sum += int(m)
#         a = a - m * 2
#         m = int(a / 3)
#     if a + 1 == 3:
#         sum += 1
# print sum

# ar = [10, 20, 32, 12, 32, 45, 11, 21, 31, 41, 33]
# mount = [0] * len(ar)
# sum_count = 0
# dc = 0
# ac = 0
# eq = 0
# for i in xrange(0, len(ar) - 1):
#     if ar[i] > ar[i + 1]:
#         dc += 1
#         for j in xrange(i - ac, i):
#             mount[j] = j - (i - ac) + 1
#         mount[i] = ac + 1
#         sum_count += (1 + ac + 1) * ac / 2
#         ac = 0
#     elif ar[i] == ar[i + 1]:
#         if ac > 0:
#             sum_count += ac
#             for j in xrange(i - ac, i):
#                 mount[j] = j - (i - ac) + 1
#                 mount[i] = ac + 1
#                 sum_count += (1 + ac) * ac / 2
#                 ac = 0
#             ac = 0
#
#         else:
#             sum_count += 1
#
# else:
#     ac += 1
# for j in xrange(i - dc + 1, i):
#     mount[j] = i - j + 1
# mount[i] = 1
# sum_count += (1 + dc) * dc / 2
# dc = 0
#
# print sum_count

# 学号问题
# n=int(raw_input())
# n=3
# l=[0]*(1001)
# for i in xrange(0,n):
#     no=int(raw_input())
#     l[no]+=1
# for i in xrange(0,len(l)):
#     if l[i]>0:
#         print i

def switch(c):
    dir = {'A': 10,
           'B': 11,
           "C": 12,
           "D": 13,
           'E': 14,
           "F": 15
           }
    print c
    print dir.keys()
    return dir.get("E")


str = raw_input()
ar = str.split("0x")
sum = 0
print ar[1]
for i in xrange(0,len(ar[1])-1):
    sum += pow(16, i) * switch(ar[1][i])
print sum
