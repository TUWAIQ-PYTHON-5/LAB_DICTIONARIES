   
phone_book={"Amal":"0568323222" ,"Mohammed":"0568323222","Khadijah":"0532335983","Abdullah":"0545341144"," Rawan":"0545534556"," Faisal":"0560664566","Layla":"0567917077"}
user=input("Write the number:")
phone_book = phone_book.values()
if user in phone_book:
    print("the owner")
else:
    print("Sorry, the number is not found")

if user<"10" or user>"10" :
   print("This is invalid number")
if user==str or user== "@ # % &": 
   print(" This is invalid number")

   
lst=[5, 0, 34, 9, 0, 13, 8]
def lst_func(my_list:list):
    aranges_list=[nonZero for nonZero in my_list if nonZero!=0]+[Zero for Zero in my_list if Zero==0]
    return aranges_list
print(lst_func(lst))


       
   
   
