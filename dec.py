book_number = {"Amal": '0568323222', "Mohammed":'0522222232', "Khadijah": '0532335983', "Abdullah": '0545341144', "Rawan":'0545534556', "Faisal": '0560664566', "Layla": '0567917077'}

def getOwnerPhone(phoneNumber) :
    if len(str(phoneNumber)) == 10 and str(phoneNumber).isdigit():
       for element in book_number:
            if book_number[element] == phoneNumber:
                 return element
            else:
                sorry = "Sorry,the number is not found"
                return sorry
    else:
        return "This is invalid number"


phoneNumber = input('please enter phone number : ')
print(getOwnerPhone(phoneNumber))

def rearranges(numberList: list) -> list:
    listnu = [5, 0, 34, 9, 0, 13, 8]
    numberList = [numberList[i] for i in listnu]
    return numberList

print(rearranges)