# Q1
phoneBook = {"0568323222" : "Amal", "0522222232" : "Mohammed", "0532335983" : "Khadijah",
"0545341144" : "Abdullah", "0545534556" : "Rawan", "0560664566" : "Faisal", "0567917077" : "Layla"}
phoneNumber = input("Enter the phone numebr: ")

# - If the number exists, print the owner. Otherwise, print "Sorry, the number is not found".
# print(len(phoneNumber))
# print(phoneNumber.isdigit())
if phoneNumber.isdigit() :
    if len(phoneNumber) == 10 :
        if phoneNumber in phoneBook :
            print(phoneBook[phoneNumber])
        else : 
            print("Sorry, the number is not found")
    else :
        print("This is invalid number") 
else :
    print("This is invalid number")


# Q2
def rearranges(list) :
    for index1, number1 in enumerate(list) :
        for index2, number2 in  enumerate(list):
            if number1 > number2 : 
                temp = list[index1]
                list[index1] = list[index2]
                list[index2] = temp
                # print(list)
                # print("--------")
    return list
    


print(rearranges([5, 0, 34, 9, 0, 13, 8]))



