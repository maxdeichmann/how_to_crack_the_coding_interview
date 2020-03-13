def string_compression(st):
    new_string = ""
    i = 0
    st_list = list(st)
    
    while i < len(st_list):
        if len(new_string) < len(st):
            for y in range(i,len(st)):
                if st[y] is not st[i] or y == len(st_list) - 1:
                    sub_string = st[i:y]
                    new_string = new_string + st_list[i] + str(len(sub_string))
                    i += len(sub_string) - 1

                    if y == len(st_list) - 1:
                        return new_string
                    else:
                        break
            
        else:
            return st
        i += 1
    
    return st



print(string_compression("aaaabnnnnbbrewtnmmnnnnnnn"))