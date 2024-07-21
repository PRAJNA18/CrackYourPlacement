s = input()
c = {}
for i in s:
    c[i] = 1 + c.get(i, 0)

for k, v in c.items():
    if v > 1:
        print(k + " count: " + str(v))