with open("input.txt") as f:
    inp = f.readlines()
inp = [x.strip() for x in inp]

grpans = []
res = 0

#part1
# def getuniquefrommultiset(grpans):
#     unitedgrpans = ""
#     uniqueset = ""
#     for x in grpans:
#         unitedgrpans += x
#     for k in unitedgrpans:
#         if k not in uniqueset:
#             uniqueset += k
#     return len(uniqueset)
#
#
# for x, i in enumerate(inp):
#     if i:
#         grpans.append(i)
#         if x == len(inp)-1:
#             res += getuniquefrommultiset(grpans)
#         continue
#     if not(i):
#         res += getuniquefrommultiset(grpans)
#         grpans = []


