#Q1
phoneBook = {"amal": "0568323222","Mohammed": "0522222232","Khadijah": "0532335983","Abdullah": "0545341144","Rawan": "0545534556","Faisal": "0560664566","Layla": "0567917077"}

numberSearch = input("Enter the number: ")
counter = 0
for number in phoneBook:
    if len(numberSearch) > 10 or len(numberSearch) < 10:
        print("This is invalid number")
        break
    if not numberSearch.isdigit():
        print("This is invalid number")
        break
    if numberSearch == phoneBook[number]:
        print(number)
        break
    elif numberSearch != phoneBook[number]:
        counter += 1
        continue
if counter == len(phoneBook):
    print("Sorry, the number is not found")

#Q2
def rearrange(numberList):
    counter=-1
    print(counter)
    zeroList =[0]
    for number in numberList:
        counter+=1
        if number == 0:
            del numberList[counter]
            numberList +=zeroList
        else:
            continue
        if counter > len(numberList):
            break
    return numberList

print(rearrange([5, 0, 34, 9, 0, 13, 8]))