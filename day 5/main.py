with open("input.txt") as f:
    inp = f.readlines()
inp = [x.strip() for x in inp]

# part 1
# highest = 0
#
# def convert(s, higher):
#     b = ""
#     for i in s:
#         if i == higher:
#             b += "1"
#         else:
#             b += "0"
#     return int(b, 2)
#
#
# for i in inp:
#     row = i[0:7]
#     seat = i[7:]
#     row = convert(row, "B")
#     seat = convert(seat, "R")
#     id = row * 8 + seat
#     if id>highest:
#         highest = id

