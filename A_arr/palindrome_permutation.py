def palindrome_permutation(st):

    st = [element for element in st if element != " "]
    is_even = True if len(st) % 2 == 0 else False

    st_set = set(list(st))
    occurrences = []

    for character in st_set:
        occurrences.append(st.count(character))

    if is_even:
        return all([element == occurrences[0]for element in occurrences])
    else:
        occurrences_set = set(occurrences)
        if len(occurrences_set) == 2:

            return True if occurrences.count(list(occurrences_set)[0]) == 1 or occurrences.count(list(occurrences_set)[1]) == 1 else False


print(palindrome_permutation("taco cat"))
print(palindrome_permutation("taco catu"))