def value_name(number):
    phone_book={'0568323222':'Amal','05632322':'mohaamad'}
    if not number.isdigit() or len(number)!=10:
        return"This is invalid number"
    return phone_book.get(number,"sorry, the number is not found")
phone_book=input("enter number")
print(value_name(phone_book))






def number_of_funcation(number:list):
    number.sort(reverse=True)
    return number
print(number_of_funcation([5, 0, 34, 9, 0, 13, 8]))