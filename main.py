phoneBook:dict={
'Amal':'0568323222',
'Mohammed':'0522222232',
'Khadijah':'0532335983',
'Abdullah':'0545341144',
'Rawan':'0545534556',
'Faisal':'0560664566',
'Layla':'0567917077'
}

#listOfnumber:list=list(phoneBook.values())
phonenumber:str=input('Enter phone number: ')

while  not len(phonenumber) ==10 or not phonenumber.isdigit():
    print("This is invalid number")
    phonenumber:str=input('Please Re-Enter phone number: ')

for name,number in phoneBook.items():
    if phonenumber==number:
        print ("The Owner is : ",name,number)
        break
if not phonenumber==number:
    print("Sorry, the number is not found")


def orderByzero(listOfnumbers:list)->list:
    zeroList:list=[]
    allNumbers:list=[]

    for number in listOfnumbers:
        if number==0:
            zeroList.append(number)
        else:
            allNumbers.append(number)
    allNumbers.extend(zeroList)
    return allNumbers

print(orderByzero([5, 0, 34, 9, 0, 13, 8]))




