for n in range(0,151):
    print(n)

for m in range(5,1001,5):
    print(m)

for c in range(1,101):
    if c % 10 == 0:
        print("Coding Dojo")
    elif c % 5 == 0:
        print("Coding")
    else:
        print(c)

sum = 0
for w in range(1,500000,2):
    sum += w
print(sum)

for f in range(2018,0,-4):
    print(f)

lowNum = 3
highNum = 28
mult = 3
for l in range(lowNum,highNum):
    if l % mult == 0:
        print(l)