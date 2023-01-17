#phone_book = {
 #   "":  , : ,
  #   "Khadijah":0532335983 ,"Abdullah":0545341144 ,
   #  "Rawan":0545534556, "Faisal":0560664566,"Layla":0567917077}

def get_name(number:str):
    phone_book ={
        '0568323222':"Amal","0522222232":"Mohammed"
    }
    if not number.isdigit() or len(number)!= 10:
        return("this is invaled number")
    elif phone_book.get(number)==None:
        return "sorry,"
    else:
        return phone_book.get(number)

phone_book= input("enter number")
print(get_name(phone_book))

# = = = = = = 

def zero_to_left(list1:list):

    list1.sort(reverse=True)
    return list1

print(zero_to_left([5, 0, 34, 9, 0, 13, 8]))
