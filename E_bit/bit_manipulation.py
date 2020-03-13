def insertion(n,m,i,j):
    return bin(((((n>>j)<<m.bit_length()) | m)<<i) | n)


def binary_fract_to_string(num):
    out = []
    ev = 0
    while ev != 1:
        ev = num * 2
        if ev >= 1:
            out.append(1)
        else:
            out.append(0)
        num = ev % 1
    return "".join([str(e) for e in out])



def binary_to_string(num):
    out = []
    while num > 0:
        if num % 2 == 0:
            out.append(0)
            num = num/2
        else:
            out.append(1)
            num = (num-1) / 2
    out.reverse()
    return "".join([str(e) for e in out])

def flip_bit_to_win(num):
    out = {}
    num_str = binary_to_string(num)
    for i, bit in enumerate(num_str):
        if bit == "0":
            test_list = list(num_str)
            test_list[i] = "1"
            longest = 0
            for start in range(len(test_list)):
                for end in range(start, len(test_list)):
                    test_set = set(test_list[start:end+1])
                    if not "0" in test_set and len(test_set) == 1:
                        if end - start > longest:
                            longest = end - start
            out[i] = longest

    return max(out, key=out.get)

def next_number(num):

    # calculate p, c, c0, c1
    c0 = 0
    c1 = 0
    c = num

    while (c & 1) == 0 and c != 0:
        print(">>>", bin(c&1))
        c0 += 1
        c = c >> 1
        print("---", c0, bin(c))

    while (c & 1) == 1 and c != 0:
        c1 += 1
        c = c >> 1
        
    print(c0, c1)

    p = c1 + c0
    return [get_next(num,p, c0, c1), get_prev(num,p, c0, c1)]

def get_prev(num, p, c0, c1):
    mask = 1 << c0
    num = num ^ mask

    mask = 1 << (c0-1)
    num = num | mask
    return num


def get_next(num, p, c0, c1):
    num = num | (1 << p)


    print(bin(num))
    a = 1 << p # all zeros except for a 1 at position p.
    b = a - 1 # all zeros, followed by p ones.
    mask = ~b # all ones, followed by p zeros.
    num = num & mask # clears rightmost p bits.

    a = 1 << (c1 - 1)
    b = a - 1
    num = num | b

    return num


def num_of_flips(a,b):
    difference = a^b
    count = 0
    while difference != 0:
        count += difference & 1
        difference = difference >> 1
    return count

def pairwise_swap(num):
    right = (0xaaaaaaaa & num) >> 1
    left = (0x55555555 & num) << 1
    return bin(right | left)


def draw_line(screen, width, x1, x2, y):

    print("input: ", [str(bin(e)) for e in screen])

    sub = screen[y*width:(y+1)*width]

    for byte_index in range(x1,x2):
        element_index = int(byte_index/8)
        pixel_in_element = byte_index + 1 - element_index * 8
        print(pixel_in_element)
        element = sub[element_index]
        mask = 1 << (8 - pixel_in_element)
        sub[element_index] = element | mask

    screen[y*width:(y+1)*width] = sub
    return [str(bin(e)) for e in screen]

# print(insertion(0b10000000010, 0b10011, 2, 6))
# print(binary_fract_to_string(0.890625))
# print(binary_to_string(100))
# print(binary_to_string(36))
# print(flip_bit_to_win(1775))
# print([(bin(e),e) for e in next_number(13948)])
# print(num_of_flips(90, 51))
# print(pairwise_swap(5737))

# screen = [0xAA,0xAA,0xAA,0xAA,0xAA,0xAA]
# print("output: ", draw_line(screen, 2, 4, 10, 1))