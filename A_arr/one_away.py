def one_away(one, two):
    one_list = list(one)
    two_list = list(two)

    if one == two:
        return True
    elif len(one) == len(two) + 1:
        # two is shorter -> insert into two
        for i in range(len(one)):
            if i < len(two):
                if one_list[i] is not two_list[i]:
                    two_list.insert(i, one_list[i])
                    break
            elif len(one_list) != len(two_list):
                two_list.append(one_list[-1])
        return one_list == two_list
    elif len(one) == len(two) - 1:
        # one is shorter -> remve from
        for i in range(len(two)):

            if i < len(one):
                if one_list[i] is not two_list[i]:
                    one_list.pop(i)
                    break
            else:
                two_list.pop(-1)
        return one_list == two_list
    elif len(one) == len(two):
        # edit in one
        for i in range(len(one)):
            if one_list[i] is not two_list[i]:
                two_list[i] = one_list[i]
                break
        return one_list == two_list
    else:
        return False






print(one_away("pale", "ple")) #true
print(one_away("pales", "pale")) #true
print(one_away("pale", "bale")) #true
print(one_away("pale", "bake")) #false