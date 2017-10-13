
l=[] this is the list declaration
c=0
while c<10:
    n=int(input("enter no.:"))
    l.append(n)
    c=c+1
    for i in l:
        if i%2==0:
            print("is even")
        else:
            print("is odd")
            
                
