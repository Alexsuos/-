def kard(a):
    a1=a
    b=len(str(a))
    b1=[]
    if b==16:
        c=0
        for i in a1:
            if c<12:
                b1.append("*")
            else:
                b1.append(a[c])
            c+=1
    return ("".join(b1))

print(kard(input("Ввкдите номер вашей карты")))




