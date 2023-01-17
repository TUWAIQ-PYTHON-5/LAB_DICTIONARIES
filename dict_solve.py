def phone_dict (number):
    phone_book = {
        "0568323222"  : "Amal"
        ,"0522222232" :"Mohammed"
        , "0532335983":"Khadijah" 
        ,"0545341144" : "Abdullah" 
        ,"0545534556" :"Rawan" 
        ,"0560664566" :"Faisal"
        ,"0567917077" :"Layla" 
        }
    if not number.isdigit() or len(number) != 10:
        return("this is invalid number ")
    elif phone_book.get(number)==None :
        return "Sorry, the number is not found"
    else :
        return phone_book.get(number)
phone_book=input("please enter phone number: ")
print(phone_dict(phone_book))



def arranged_list(list_numbers: list ):
    list_numbers.sort  (reverse =True)
    return list_numbers
print(arranged_list([5, 0, 34, 9, 0, 13, 8]))

