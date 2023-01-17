   

def get_name(number):
    phone_book={"0568323222":"Amal" ,
    "0568323222":"Mohammed",
    "0532335983":"Khadijah",
    "0545341144":"Abdullah",
    "0545534556":" Rawan"
    ,"0560664566":" Faisal"
    ,"Layla":"0567917077"}

    if not number.isdigit() or len(number)!=10 :
        return "This is invalid number"
    elif phone_book.get(number)==None :
        return "Sorry, the number is not found"
    else  :
        return phone_book.get(number)
                            
phone_number=input("Enter phone number ")
print (get_name(phone_number))



   # Q2:Write a function that receives a list containing the following numbers : 
lst=[5, 0, 34, 9, 0, 13, 8]
def lst_func(my_list:list):
    aranges_list=[nonZero for nonZero in my_list if nonZero!=0]+[Zero for Zero in my_list if Zero==0]
    return aranges_list
print(lst_func(lst))

       
   
   
