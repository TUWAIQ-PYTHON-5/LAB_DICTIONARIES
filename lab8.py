def my_listpass(my_list:list):
    my_list.sort(reverse= True)
    return my_list



phone_book ={"0568323222": "Amal" ,"0522222232" : "Mohammed", "0532335983": "Khadijah"  , "0545341144" : "Abdullah"  ,  "0545534556" : "Rawan",  "0567917077": "Layla",   "0560664566" : "Faisal"}
find_number:int=input("enter phone number: ")

if find_number in phone_book.keys():
    print("hello ",phone_book.get(find_number))
elif len(find_number) > 10:
    print("This is invalid number")
elif not find_number.isnumeric():
    print("This is invalid number")
else:
    print("Sorry, the number is not found")


my_list=[5, 0, 34, 9, 0, 13, 8]
print(my_listpass(my_list))