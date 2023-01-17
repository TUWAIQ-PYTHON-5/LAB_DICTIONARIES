


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

phone_book1={"0568323222":"Amal","0522222232":"Mohammed","0532335983":"Khadijah","0545341144":"Abdullah","0545534556":"Rawan","0560664566":"Faisal","0567917077":"Layla"}
 
 


if not number.isdigit() or len(number)!=10 :
    print ("This is invalid number") 
elif phone_book1.get(number)==None :
        print("Sorry, the number is not found")
else  :
    print( phone_book1.get(number))







def function_1(list1):
    list1.sort(reverse=True)
    return list1

print(function_1([5, 0, 34, 9, 0, 13, 8]))




