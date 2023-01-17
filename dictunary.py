def find_num(number):
    book_phone = {'0568323222': "Amal", '0522222232': 'Mohammed',"0532335983": 'Khadijah' }

    if not number.isdigit() or len(number) != 10:
      return "This is invalid number"
      
    elif book_phone.get(number) == None:
      return "Sorry, the number is not found"
    
    else:
      return book_phone.get(number)

book_phone = input("Enter a phone number:")
print(find_num(book_phone))





lst = [5,0,34,9,0,13,8]
def move_zero(lst):
    nonzero = [x for x in lst if x !=0]
    zero = [j for j in lst if j == 0]
    return nonzero + zero


