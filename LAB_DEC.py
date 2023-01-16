
#user_inputt= input(' Enter the number please ')


phone_book = {"0568323222" : "Amal" ,
"0522222232" : "Mohammed" ,  "0532335983" : "Khadijah" , 
"0545341144" : "Abdullah" , "0545534556" : "Rawan", "0560664566" : 
"Faisal" ,"0567917077" :"Layla" }

def find_owner (number:str):
    if len(number) == 10 and number.isdigit():
        for element in phone_book:
            if  element == number:
                name_of_owner = phone_book.get(number , "Sorry, the number is not found" )
                return name_of_owner
        else:
            message = "Sorry, the number is not found"
            return message
    else:
        
        return "This is invalid number"
print(find_owner(input(" Enter a number to search in the a phone book : ")))


# Q2:Write a function that receives a list containing the following numbers :

def re_arranges(numberList : list) -> list:
    temp = []
    zeros = []

    for i in  range(len(numberList)):
        if numberList[i] != 0:
            temp.append(numberList[i])
        else:
            zeros.append(numberList[i])

    re = temp+zeros
    return re 

print(re_arranges([5, 0, 34, 9, 0, 13, 8])) 


