from functools import reduce
from random import randint

class Listy(list):
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
    
    def elementAt(self, index):
        if index > len(self) - 1:
            return -1
        else:
            return self[index]
    def len(self):
        return NameError

def group_anagrams(arr):
    ana_dict = {}

    for st in arr:
        sorted_st = sort_string(st)
        if sorted_st in ana_dict:
            ana_dict[sorted_st].append(st)
        else:
            ana_dict[sorted_st] = [st]

    return reduce(lambda x,y: x+y, ana_dict.values())

def sort_string(st):
    original_list = list(st)
    for j in range(len(original_list)):
        for i in range(len(original_list)-1):
            if original_list[i] > original_list[i+1]:
                temp = original_list[i+1]
                original_list[i+1] = original_list[i]
                original_list[i] = temp

    return "".join(original_list)


def search_rotated_arr(arr, element):
    if len(arr) < 2:
        return arr
    else:
        count = 0
        while arr[0] > arr[-1]:
            first_element = arr.pop(0)
            arr.append(first_element)
            count += 1
        ind = binary_search_ind(arr, element, 0, len(arr)-1)
        return ind - (count+2) if ind >= (count+1) else ind + count


def binary_search_ind(arr, element, start_index, end_index):
    mid = int((len(arr)) / 2)

    if arr[mid] == element:
        return start_index+mid
    elif element < arr[mid]:
        left = arr[:mid]
        return binary_search_ind(left, element, start_index, end_index-mid)
    else:
        right = arr[mid:]
        return binary_search_ind(right, element, mid+start_index, end_index)

def binary_search(arr, element):
    mid = int(len(arr)/2)
    if arr[mid] == element:
        return element
    elif element < arr[mid]:
        # left
        return binary_search(arr[:mid], element)
    else:
        return binary_search(arr[mid:], element)



def find_without_size(arr, element):
    # first find the length
    if arr == None:
        return None
    elif arr.elementAt(0) == element:
        return 0
    else:
        # find upper boun
        upper_bound = 0
        val = arr.elementAt(0)
        exponent = 0
        while val > 0:
            exponent += 1
            upper_bound = 2**exponent
            val = arr.elementAt(upper_bound-1)

        # find lower bound
        lower_bound = 2**(exponent-1)
        print(lower_bound, upper_bound)

        final_value = arr.elementAt(upper_bound)
        post_final_value = arr.elementAt(upper_bound+1)
        index = upper_bound

        difference = upper_bound - lower_bound

        final_index = -1
        for index in range(lower_bound, upper_bound):
            if arr.elementAt(index) >= 0 and arr.elementAt(index+1) == -1:
                final_index = index

            
        print(final_index)
        
        return binary_search(arr[:final_index+1], element)


def binary_sparse_search(arr, element):
    mid = int(len(arr)/2)
    if arr[mid] == "":
        found = False
        lower = mid
        upper = mid
        while found == False and (lower >= 0 or upper < len(arr)):
            lower -= 1
            upper += 1
            if upper < len(arr) and arr[upper] != "":
                found = True
                mid = upper
            elif lower >= 0 and arr[lower] != "":
                found = True
                mid = lower
    
    if arr[mid] == element:
        return element
    elif arr[mid] > element:
        return binary_sparse_search(arr[:mid], element)
    else:
        return binary_sparse_search(arr[mid:], element)


def sort_20GB_file(file):
    pass
    # 20 gb are a lot, so we do not want to load all of this into memory.
    # divide the larger file into smaller ones e.g.100
    # additionally, create one file for every letter in the alpha -> 26 files
    # => 20/26 = 0,78 gb per file
    # => go through all 100 files and append the strings to the files depending on the first letter
    # => go through all letter files and sort the strings in there


def missing_int(file):
    pass
    # find any missing int among four billion non-negative integers
    # there is 1gb memory available to solve this
    # one int is 16 bit -> 2 byte per number
    # 8 billion byte -> 1 gb for 1 b bytes -> 8GB filesize
    # split file up in equal parts


def find_missing_int(arr, maxValue, intLength):
    # 16 is size of an int
    nrOfElements = int(maxValue / intLength) if maxValue % intLength == 0 else int(maxValue / intLength) + 1
    results_arr = [0 for element in range(0, nrOfElements)]

    # assign elements
    for element in arr:
        bucket = int(element / intLength)
        index = intLength - (element % intLength)
        results_arr[bucket] = results_arr[bucket] | 1 << index - 1
    
    print([bin(element) for element in results_arr])

    
    # find first 0
    for index, element in enumerate(results_arr):

        next_max_val = 2 ** intLength
        mask = next_max_val - 1
        xor = element ^ mask

        bit_count = 0
        
        while xor > 1:
            bit_count += 1
            xor = xor >> 1

        if bit_count > 0:
            return (intLength - bit_count - 1) + (index * intLength)

def duplicate_finder(arr):
    duplicates = []
    bit_storage = [0 for element in range(0,int(32000/64))]
    for element in arr:
        bucket = int(element/64)
        index = element % 64
        mask = 1 << (64 - index)
        new_bucket = bit_storage[bucket] | mask
        # print(bucket, index, bin(mask), bin(new_bucket))
        if new_bucket == bit_storage[bucket]:
            duplicates.append(element)
        else:
            bit_storage[bucket] = new_bucket
    #print([bin(e) for e in bit_storage])
    return sorted(duplicates)

def sorted_matrix_search(matrix, element):
    print("sorted_matrix_search", matrix)
    mid = int(len(matrix)/2)
    if element >= matrix[mid][0] and element <= matrix[mid][-1]:
        return binary_search(matrix[mid], element)
    elif element < matrix[mid][0]:
        return sorted_matrix_search(matrix[:mid], element)
    else:
        return sorted_matrix_search(matrix[mid:], element)


    
class Node(object):
    def __init__(self, value):
        super().__init__()
        self.value = value
        self.left = None
        self.right = None
    
    def print_tree(self):
        if self.left is not None:
            self.left.print_tree()
        print(str(self.value))
        if self.right is not None:
            self.right.print_tree()
    
    def __str__(self):
        output = str(self.value)
        if self.left is not None:
            output += " l: " + str(self.left.value)
        if self.right is not None:
            output += " r: " + str(self.right.value)
        return output
        
class Structure(object):

    def __init__(self):
        super().__init__()
        self.struct = None

    def track(self, value):
        if self.struct is None:
            self.struct = Node(value)
        else:
            unassigned = True
            current_node = self.struct
            while unassigned == True:
                    
                if value < current_node.value:
                    if current_node.left is not None:
                        current_node = current_node.left
                    else:
                        current_node.left = Node(value)
                        unassigned = False
                else:                       
                    if current_node.right is not None:
                        current_node = current_node.right
                    else:
                        current_node.right = Node(value)
                        unassigned = False
    
    def print_tree(self):
        return self.in_order_traversal(self.struct)


    def in_order_traversal(self, node):
        if node.left is not None:
            self.in_order_traversal(node.left)
        print(node.value)
        if node.right is not None:
            self.in_order_traversal(node.right)


    def getRankOfNumber(self, value):
        return self.counting_traversal(self.struct, value)

    def counting_traversal(self, node, value):
        count = 1
        print("node: ", node)
        if node.left is not None:
            count += self.counting_traversal(node.left, value)
        if node.value == value:
            return count - 1
        if node.right is not None:
            count += self.counting_traversal(node.right, value)
        return count





def find_peaks_and_valleys(arr):
    output = []
    find_max = True

    while len(arr) > 0:

        if find_max == True:
            val = -1
            index = -1
            
            for i, element in enumerate(arr):
                if element > val:
                    val = element
                    index = i
        
        if find_max == False:
            val = 2**64
            index = -1

            for i, element in enumerate(arr):
                if element < val:
                    val = element
                    index = i
        arr.pop(index)
        output.append(val)
        find_max = not find_max
    return output






if __name__ == "__main__":
    # anagrams = ["apple", "uz","üpoiuztrewq" "aplpe", "zu", "qwertzuiopü"]
    # print(group_anagrams(anagrams))

    # rotated_arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
    # print(search_rotated_arr(rotated_arr, 15))

    # arr = Listy([randint(0, 99) for element in range(0,100)])
    # print(find_without_size(Listy(rotated_arr), 5))


    # sparse_arr = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
    # print(binary_sparse_search(sparse_arr, "car"))

    # max_val = 2**9
    # ints = [randint(0,max_val-1) for element in range(0,1000)]
    # print("final: ", find_missing_int(ints, max_val, 64))

    # ints = [randint(0,32000-1) for element in range(0,32000)]
    # uniques = set(ints)
    # final = []
    # for element in uniques:
    #     if ints.count(element) > 1:
    #         final.append(element)
    # final = sorted(final)
    # print(final[:20])
    # print(duplicate_finder(ints)[:20])
    

    # matrix = [
    #     [1,2,3,4],
    #     [5,6,7,8],
    #     [9,10,11,12],
    #     [13,14,15,16],
    # ]

    # print(sorted_matrix_search(matrix, 10))


    # struct = Structure()
    # stream = [5,1,4,4,5,9,7,13,3]
    # for element in stream:
    #     struct.track(element)
    # struct.print_tree()
    # print(struct.getRankOfNumber(13))


    print(find_peaks_and_valleys([randint(0, 99) for element in range(0,10000)]))