import random
try:
    i=input("Enter Base Word/s:")
except len(i)>20:
    print("exceeding word limit")
finally:
    l=[]
    for a in i:
        l.append(a)
    for b in ['!','@','#','$','%']:
        l.append(b)
    p=""
    for c in range(0,len(l)):
        passwd=random.choice(l)
        p=p+passwd
    print("Safer Password:", p)
input()
