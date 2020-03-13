def urlify(st):
    return "".join([ch if ch != " " else "%20" for ch in list(st)])



st = "Mr John Smith"

print(urlify(st))