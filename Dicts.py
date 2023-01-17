#Q1
def numQuery(phNum : str):
    print 
    if (len(phNum) != 10): 
        print("This is invalid number")
        return
    if (not phNum.isnumeric()):
        print("This is invalid number")
        return

        
    numGuide = {"0568323222":"Amal",
                "0522222232":"Mohammed",
                "0532335983":"Khadijah",
                "0545341144":"Abdullah",
                "0545534556":"Rawan",
                "0560664566":"Faisal",
                "0567917077":"Layla",}

    for key, value in numGuide.items():
        #print(key)
        if phNum == key:
            print(value)
            break
    else: print("Sorry, the number is not found")
        
        #else: print("This is invalid number")


usrNum : str = input("Enter Phone No.")
numQuery(usrNum)

print("##############################")

#Q2
def rearr (lis : list) ->list:
    #print(lis)
    swap=[]
    last=[]
    
    i:int =0
    for i in range(len(lis)):
            if (lis[i] == 0):
                swap.append(lis[i])
                #print(lis[i+1])
                #lis.append(swap[i-1])
            else:
                last.append(lis[i])
                #continue
                #swap.append([i+1])
                #lis[i]=swap
                #print(i)
            
    print(last)
    print(swap)
    last+=swap
    return last

usrList = [5, 0, 34, 9, 0, 13, 8]
print(rearr(usrList))

