q = "a_example.in"
w = "b_small.in"
r = "c_medium.in"
t = "d_quite_big.in"
y = "e_also_big.in"

files = [q,w,r,t,y]
for file in files:

    with open(file,"r") as f:
        a = list()
        for line in f:
            line = line.strip()
            line = line.split()
            a.append(line)
        
    ms = a[0][0] # max number of slice we can have
    ms = int(ms)

    tp = a[0][1] #total number of pizza we can have
    tp = int(tp)

    w = a[1]
    #w.sort(reverse = True)

    #changing string in w to integer
    for i in range(len(w)):
        w[i] = int(w[i])    


    ind = list()
    lind = list()
    los = list()

    for j in range(len(w)):
        s =0
        ind = []
        #print(j)
        for i in range(len(w)-1-j,-1,-1):
            #print(i)
            s += w[i]

            if s < ms:
                ind.append(i)
                continue
    
            elif s == ms:
                ind.append(i)
                break
        
            elif s > ms:
                s -= w[i]
        #print()        
        los.append(s)        
        lind.append(ind)       
        
    #print(los)
    #print(lind)

    os = max(los) # it the total number of slice we wil order
    #print(os)

    d = los.index(os)# index of max number of slice
    #print(d)

    e =lind[d] #e is final indexes for slices
    e.sort()
    #print(e)
    z = len(e) # number of pizza we will order
    file = file.replace("in","out")
    print(file)
    
    with open(file,"w") as f:
        z = str(z)
        f.write(z)
        f.write("\n")
        for i in e:
            i = str(i)
            f.write(i)
            f.write(" ")