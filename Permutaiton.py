def rec(n,line) :
    
    if n >= 3 :
        print(line)
        return
    
    for i in range(3) :
        line = line + str(i)
        rec(n+1,line)
        line = line[:-1]
    

rec(0,"")