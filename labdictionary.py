#Q1
def get_name(number):
    phone_book = { '0568323222': "Amal",'0522222232' : "Mohammad", }

    if not number.isdigit() or len(number)!=10 :
        return "This is invalid number"
    elif phone_book.get(number)==None :
        return "Sorry, the number is not found"
    else  :
        return phone_book.get(number)
                            
phone_number=input("Enter phone number ")
print (get_name(phone_number))
    
#Q2
def function(my_list):
    return list(reversed(sorted(my_list)))
print(function ([5, 0, 34, 9, 0, 13, 8]))   