# a = [5, 3, 45, 3, 4]
#
#
# def quicksort(a):
#     if len(a) <= 1:
#         return a
#     l = [x for x in a[1:] if x <= a[0]]
#     r = [x for x in a[1:] if x > a[0]]
#     return quicksort(l) + [a[0]] + quicksort(r)
#
#
# print str(a)
# a = quicksort(a)
# print str(a)
import datetime

print datetime.datetime.strptime("2017-07-21","%Y-%m-%d").strftime("%Y%m%d")