


'''
| Name    | Number      |
| -------- | ---------- |
| Amal     | 0568323222 |
| Mohammed | 0522222232 |
| Khadijah | 0532335983 |
| Abdullah  | 0545341144 |
| Rawan    | 0545534556 |
| Faisal   | 0560664566 |
| Layla    | 0567917077 |

'''
number=str(input("Enter the number:"))
phone_book1={"Amal":"0568323222","Mohammed":"0522222232","Khadijah":"0532335983","Abdullah":"0545341144","Rawan":"0545534556","Faisal":"0560664566","Layla":"0567917077"}
 
number_2=int(number) 
if number_2>10 and number_2<10:
     print ("This is invalid number")





while number =="0568323222":
  print("the name of the owner is Amal")
  break
while number =="0522222232":
  print("the name of the owner is Mohammed")
  break
while number =="0532335983":
  print("the name of the owner is Khadijah")
  break
while number =="0545341144":
  print("the name of the owner is Abdullah")
  break
while number =="0545534556":
  print("the name of the owner is Rawan")
  break
while number =="0560664566":
  print("the name of the owner is Faisal")
  break
while number =="0567917077":
  print("the name of the owner is Layla")
  break
else :
  print( "Sorry, the number is not found")



def function_1(list1):
    list1.sort(reverse=True)
    return list1

print(function_1([5, 0, 34, 9, 0, 13, 8]))




