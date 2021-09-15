from typing import List
'''
Quick Sort
    Array = [0,5,1,8,9,7,2]
    Remove any element from an array called as pivot element.
    pivot = 5
    - iterate over array
    - if any element is grater than pivot, then add to another sub-array i.e greater = []
    - else add to another sub-array i.e lower = []
    - and do it subsequet

'''


def quick_sort(seq: List,/):
    lower = []
    greater = []

    if len(seq) <= 1:
        return seq
    else:
        pivot = seq.pop()
    
    for i in seq:
        if i > pivot:
            greater.append(i)
        else:
            lower.append(i)
    
    return quick_sort(lower) + [pivot] + quick_sort(greater)


if __name__ == '__main__':
    print(quick_sort([0,5,1,8,9,7,2]))
