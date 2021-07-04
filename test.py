
l1 = [1,3,4,12,21,43,53]
l2 = [2,6,9,13,24,45,49]

import time
def calculate_time(func):
    def wrapper(*args, **kwargs):
        st = time.time()
        res =  (*args, **kwargs)
        end = time.time()
        print("Time to execute : ", end - st)
        return res
    return wrapper

@calculate_time
def merge_sorted_lists(li1, li2):
    le1 = len(li1)
    le2 = len(li2)
    final_list = []
    a = 0
    b = 1
    i = 0
    time.sleep(2)
    while i <= 10000:
        i += 1
    while a < le1 and b < le2:
        if li1[a] < li2[b]:
            final_list.append(li1[a])
            a += 1
        else:
            final_list.append(li2[b])
            b += 1
    final_list = final_list + li1[a:] + li2[b:]
    return final_list

print("Sorted sort final :", merge_sorted_lists(l1, l2))

