PhoneOwner = {

        "0568323222"  : "Amal", 
        "0522222232"  :"Mohammed" ,
        "0532335983"  : "Khadija" ,
        "0545341144"  : "Abdullah",
        "0545534556"  :"Rawan" ,
        "0560664566"  :"Fisal"  ,
        "0567917077"  : "Layla"
     }

count = 0
numbers = "1234567890"
flag = True

input_ = input("Enter phone number: ")
for i in input_:
  count = count + 1
  if i not in numbers:
    print("This is invalid number ")
    flag = False
    break
  elif len(input_) < 10 or len(input_) > 10:
    print("This is invalid number  ")
    flag = False
    break

if input_ not in PhoneOwner and flag == True:
   print("Sorry, The number is not found")
elif flag:
    print(PhoneOwner[input_])
print("--------------------------------")     


def rearrange( arr : list ):
    n = len( arr )
    temp = 0
    for i in range(n) :
        for j in range(n - 1) :

            if arr[j] < arr[j + 1] :
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr

list_ = [5,0,34,9,0,13,8]
print(rearrange(list_))






