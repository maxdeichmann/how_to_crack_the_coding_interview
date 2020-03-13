from design_patterns.decorator.timer_function import timer
from random import randint
from math import log, floor

@timer
def bubble_sort(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
    return arr

@timer
def selection_sort(arr):
    for i in range(0, len(arr)-1):
        minimum_value = 100000000
        minimum_index = 100000000
        for j in range(i, len(arr)):
            if arr[j] < minimum_value:
                minimum_value = arr[j]
                minimum_index = j
        arr[minimum_index] = arr[i]
        arr[i] = minimum_value
    return arr


@timer
def merge_sort_timed(arr):
    # print("merge_sort_timed: ", arr)
    return merge_sort(arr)

def merge_sort(arr):

    if len(arr) > 1:
        middle = int(len(arr) / 2)
        left_merged = merge_sort(arr[:middle])
        right_merged = merge_sort(arr[middle:])
        
        right_index = 0
        left_index = 0
        i = 0

        while right_index < len(right_merged) and left_index < len(left_merged):
            if left_merged[left_index] <= right_merged[right_index]:
                arr[i] = left_merged[left_index]
                left_index += 1
                i += 1
            elif left_merged[left_index] > right_merged[right_index]:
                arr[i] = right_merged[right_index]
                right_index += 1
                i += 1
        while right_index < len(right_merged):
            arr[i] = right_merged[right_index]
            right_index += 1
            i += 1
        while left_index < len(left_merged):
            arr[i] = left_merged[left_index]
            left_index += 1
            i += 1

    return arr


@timer
def quick_sort_timed(arr):
    # print("quick_sort_temp: ", arr)
    return quick_sort(arr)

def quick_sort(arr):
    if len(arr) > 1:
        last_element = arr[-1]
        left = []
        right = []

        for i in range(0,len(arr)-1):
            if arr[i] <= last_element:
                left.append(arr[i])
            else:
                right.append(arr[i])

        left_sorted = []
        right_sorted = []
        if len(left) > 0:
            left_sorted = quick_sort(left)
        if len(right) > 0:
            right_sorted = quick_sort(right)

        return left_sorted + [last_element] + right_sorted
    return arr


@timer
def redix_sort_timed(arr):
    return redix_sort(arr)

def redix_sort(arr):
    return arr


def counting_sort(arr, digit, radix):
    # Step 1
    A = arr
    C = [0] * radix
    B = [0] * len(A)
    

    # Step 2
    for i in range(0, len(A)):
        digit_of_Ai = int((A[i]/radix**digit)%radix)
        C[digit_of_Ai] += 1
    
    # Step 3
    for i in range(1, len(C)):
        C[i] = C[i] + C[i - 1]
    
    # Step 4
    for i in range(len(A)-1, -1, -1):
        digit_of_Ai = int((A[i]/radix**digit)%radix)
        C[digit_of_Ai] -= 1
        B[C[digit_of_Ai]] = A[i]

    return B

@timer
def radix_sort(arr, radix):
    #radix is the base of the number system
    #k is the largest number in the list
    k = max(arr)
    #output is the result list we will build
    output = arr
    #compute the number of digits needed to represent k
    digits = int(floor(log(k, radix)+1))
    for i in range(digits):        
        output = counting_sort(output,i,radix)

    return output


@timer
def insertion_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        if val < arr[i-1]:
            j = i
            while val < arr[j-1] and j-1 >= 0:
                arr[j] = arr[j-1]
                j -= 1
            arr[j] = val       
    return arr



if __name__ == "__main__":
    arr = [randint(0, 99) for element in range(0,10000)]
    # a = bubble_sort(arr.copy())
    # b = selection_sort(arr.copy())
    # c = merge_sort_timed(arr.copy())
    # d = quick_sort_timed(arr.copy())
    # e = radix_sort(arr.copy(), 10)
    # f = insertion_sort(arr.copy())

    # print(a == b)
    # print(b == c)
    # print(c == d)
    # print(a == b == c == d)

    print(e ==f)