def string_rotation(one, two):

    print(one, two)

    if len(one) != len(two):
        return False
    elif one == two:
        return True

    else:
        # two is the rotation of one
        start_index = 0
        
        for i in range(len(two)):
            if one[0] is two[i]:
                start_index = i
                break
        
        start = list(two)[i:len(two)]
        end = list(two)[0:i]
        return one == "".join(start) + "".join(end)



print(string_rotation("waterbottle", "erbottlewat"))