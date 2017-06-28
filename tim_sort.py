# coding:utf-8
import random

# a = list([1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 11])
# print a
# a.sort()
# print a
import sys

import time

min_run_len = 4
run_base_array = range(100)
run_len_array = range(100)
stack_size = 0
need_sort = []


def sort_m(array):
    remaining = len(array)
    start = 0
    end = remaining
    while remaining != 0:
        run_len = count_run_len(array, start, end)
        if run_len < min_run_len:
            if remaining < min_run_len:
                force = remaining
            else:
                force = min_run_len
            binary_sort(array, start, start + force, start + run_len)
            run_len = force
        print "push " + str(array[start:start + run_len])
        push_run(start, run_len)
        # print str(run_base_array[stack_size-1])+","+str(run_len_array[stack_size-1])
        start += run_len
        remaining -= run_len
        merge()
    force_merge()


def push_run(run_base, run_len):
    global stack_size
    # if len(run_len_array)==0:
    #     run_base_array.append(run_base)
    #     run_len_array.append(run_len)
    #     stack_size += 1
    #     return
    run_base_array[stack_size] = run_base
    run_len_array[stack_size] = run_len
    stack_size += 1


def merge_at(i):
    global stack_size
    # print stack_size
    base1 = run_base_array[i]
    base2 = run_base_array[i + 1]
    len1 = run_len_array[i]
    len2 = run_len_array[i + 1]
    run_len_array[i] = len1 + len2
    if i == stack_size - 3:
        run_base_array[i + 1] = run_base_array[i + 2]
        run_len_array[i + 1] = run_len_array[i + 2]
    stack_size -= 1
    # 右边最小元素在左边的位置
    k = gallop_right(need_sort, base2, base1, len1)
    print "find " + str(need_sort[base2]) + " in " + str(
        need_sort[base1:base1 + len1]) + " before " + str(
        need_sort[base1 + k])
    len1 -= k
    base1 += k
    if len1 == 0:
        return
    # 左边最大元素在右边的位置
    print "find " + str(need_sort[base1 + len1 - 1]) + " in " + str(
        need_sort[base2:base2 + len2])
    len2 = gallop_left(need_sort, base1 + len1 - 1, base2, len2)
    print " after " + str(need_sort[base2 + len2 - 1])
    if len2 == 0:
        return
    print "merge " + str(need_sort[base1:base1 + len1]) + " and " + str(
        need_sort[base2:base2 + len2])
    merge_a(need_sort, base1, len1, base2, len2)
    print "push " + str(need_sort[run_base_array[i]:run_base_array[i] + run_len_array[i]])


def merge_a(array, base1, len1, base2, len2):
    tmp1 = array[base1:base1 + len1]
    tmp2 = array[base2:base2 + len2]
    index = base1
    i = 0
    k = 0
    while i < len1 and k < len2:
        if tmp1[i] <= tmp2[k]:
            array[index] = tmp1[i]
            i += 1
        else:
            array[index] = tmp2[k]
            k += 1
        index += 1
    if i < len1:
        for x in xrange(i, len1):
            array[index] = tmp1[x]
            index += 1
    if k < len2:
        for x in xrange(i, len2):
            array[index] = tmp2[x]
            index += 1


def gallop_right(array, key, start, len):
    ofs = 1
    last_ofs = 0
    if array[key] < array[start]:
        max_ofs = start
        while ofs <= max_ofs and array[key] < array[start - ofs]:
            last_ofs = ofs
            ofs = (ofs << 1) + 1
            if ofs <= 0:
                ofs = max_ofs
        if ofs > max_ofs:
            ofs = max_ofs
        temp = last_ofs
        last_ofs = -ofs
        ofs = -temp
    else:
        max_ofs = len
        while ofs < max_ofs and array[key] >= array[start + ofs]:
            last_ofs = ofs
            ofs = (ofs << 1) + 1
            if ofs <= 0:
                ofs = max_ofs
            if ofs > max_ofs:
                ofs = max_ofs
    last_ofs += 1
    while last_ofs < ofs:
        m = last_ofs + ((ofs - last_ofs) >> 1)
        if array[key] > array[start + m]:
            last_ofs = m + 1
        else:
            ofs = m
    return ofs


def gallop_left(array, key, start, len):
    ofs = 1
    last_ofs = 0
    if array[key] > array[start]:
        max_ofs = len
        while ofs < max_ofs and array[key] > array[start + ofs]:
            last_ofs = ofs
            ofs = (ofs << 1) + 1
            if ofs < 0:
                ofs = max_ofs
        if ofs > max_ofs:
            ofs = max_ofs
    else:
        max_ofs = 1
        while ofs < max_ofs and array[key] <= array[start - ofs]:
            last_ofs = ofs
            ofs = ofs << 1 + 1
            if ofs < 0:
                ofs = max_ofs
        if ofs > max_ofs:
            ofs = max_ofs
        tmp = last_ofs
        last_ofs = -ofs
        ofs = -tmp
    last_ofs += 1
    while last_ofs < ofs:
        m = last_ofs + ((ofs - last_ofs) >> 1)
        if array[key] > array[start + m]:
            last_ofs = m + 1
        else:
            ofs = m
    return ofs


def merge():
    global stack_size
    while stack_size > 1:
        n = stack_size - 2
        # Z<=X+Y
        if n > 0 and run_len_array[n - 1] <= run_len_array[n] + run_len_array[n + 1]:
            # Z<X
            if run_len_array[n - 1] < run_len_array[n + 1]:
                n -= 1
            print  "merge at " + str(run_base_array[n]) + "," + str(run_len_array[n])
            merge_at(n)
        # X<Y
        elif run_len_array[n] <= run_len_array[n + 1]:
            merge_at(n)
            # print  "merge at " + str(run_base_array[n]) + "," + str(run_len_array[n])
        else:
            break
    return


def force_merge():
    global stack_size
    while stack_size > 1:
        n = stack_size - 2
        # Z<X merge Y,X
        if n > 0 and run_len_array[n - 1] < run_len_array[n + 1]:
            n -= 1
        print "merge at " + str(run_base_array[n]) + "," + str(run_len_array[n])
        merge_at(n)
    return


def binary_sort(array, lo, hi, start):
    for i in xrange(start, hi):
        left = lo
        right = i
        value = array[i]
        while left < right:
            mid = (left + right) >> 1
            if array[i] < array[mid]:
                right = mid
            else:
                left = mid + 1
        # print str(left)+","+str(right)
        for x in xrange(i, left, -1):
            array[x] = array[x - 1]
        array[left] = value
    return


def count_run_len(array, start, end):
    run_hi = start + 1
    if run_hi == end:
        return 1
    if array[start] < array[run_hi]:
        run_hi += 1
        while run_hi < end and array[run_hi - 1] <= array[run_hi]:
            # print array[run_hi-1]
            # print array[run_hi]
            run_hi += 1
    else:
        run_hi += 1
        while run_hi < end and array[run_hi - 1] > array[run_hi]:
            # print array[run_hi - 1]
            # print array[run_hi]
            run_hi += 1
        reverse_array(array, start, run_hi)
    return run_hi - start


def reverse_array(array, start, end):
    tmp = array[start:end]
    for x in xrange(0, len(tmp) >> 1):
        array[start + x] = tmp[len(tmp) - x - 1]
        array[end - 1 - x] = tmp[x]
        # if start + 1 == end:
        #     tmp = array[start]
        #     array[start] = array[end]
        #     array[end] = tmp
        # for i in xrange(0, (start + end) >> 1):
        #     tmp = array[i]
        #     array[start + i] = array[start + end - i]
        #     array[start + end - i] = tmp


array_len = 30
array = []
for i in xrange(0, array_len):
    array.append(i)

for i in xrange(0, array_len / 5):
    index = random.randint(0, array_len - 1)
    array[index] = random.randint(array_len, array_len * 10)
need_sort = array
# t1 = time.time()
# array.sort()
# t2 = time.time()
# print t2 - t1
# array_m = [0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 26, 26, 29, 28, 27,
#            27, 28, 29, 146, 258, 269]
# need_sort = array_m
print need_sort
sort_m(need_sort)
print need_sort
