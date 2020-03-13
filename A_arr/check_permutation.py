def check_permutation(one, two):

    one_set = set(list(one))
    two_set = set(list(two))

    if one_set == two_set:
        for key in one_set:
            if two.count(key) != one.count(key):
                return False
        return True
    else:
        return False


assert check_permutation("hallo","ollah") == True, "Should be true"
assert check_permutation("abe","abee") == False, "Should be false"
assert check_permutation("abe","abc") == False, "Should be false"
