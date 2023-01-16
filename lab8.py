def my_listpass(my_list:list):
    my_list.sort(reverse= True)
    return my_list



phone_book ={"amal": 568323222 , "Mohammed" :522222232, "Khadijah" : 532335983 , "Abdullah" : 545341144, "Rawan": 545534556, "Layla": 567917077 , "Faisal" : 560664566}
find_number:int=input("enter phone number: ")

if find_number in phone_book.values():
    print("its exist")
elif len(find_number) > 10:
    print("This is invalid number")
elif not find_number.isnumeric():
    print("This is invalid number")
else:
    print("Sorry, the number is not found")


my_list=[5, 0, 34, 9, 0, 13, 8]
print(my_listpass(my_list))