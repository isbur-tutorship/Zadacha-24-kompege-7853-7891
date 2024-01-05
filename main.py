f = open("24_7891.txt")
a = f.readlines()
megastr = ""
for x in a:
    megastr = megastr + x

maxlen = 0
for x in range(0,len(megastr)):
    for y in range(x+1, len(megastr)):
        if megastr[x] == megastr[y]:
            maxlen = max(maxlen, y-x+1)
            break

print(maxlen)