

person_number = {
"0568323222" : "amal" , 
"0522222232" : "Mohammed" , 
"0532335983" : "Khadijah" ,
"0545341144" : "Abdullah" ,
"0545534556" : "Rawan" , 
"0560664566" : "Faisal" ,
"0567917077" :"Layla"
     }

def findOwner (number:str):
    if len(number) == 10 and number.isdigit():
        for element in person_number:
            if  element == number:
                nameOfOwner = person_number.get(number )
                return nameOfOwner
        else:
            sorry = "Sorry, the number is not found"
            return sorry 
    else:
        
        return "This is invalid number"
print(findOwner(input("enter the number you want to search for : ")))



def function_1 (list1: list):
    list1.sort(reverse=True)
    return list1
print (function_1([5, 0, 34, 9, 0, 13, 8]))

