f = open('24.txt')
doc = f.readline()

alphabet = '1234567890QWERYUIPASDFGHJKLZXCVBMNOT'
for a in 'NOT':
    for b in alphabet:
        for c in 'NOT':
            substr = a+b+c
            doc = doc.replace(substr, " ")

ans = doc.split()
print(max([len(x) for x in ans]))


