i = 1
while i < 101:
    if i%7 == 0:
        i+=1
        continue
    elif i%10 == 7 or i//10 == 7 :
        i+=1        
        continue
    print(i)
    i += 1
