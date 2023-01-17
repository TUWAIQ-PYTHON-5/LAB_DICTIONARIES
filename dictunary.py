book_phone = {"Amal" : "0568323222", "Mohammed": "0522222232",
"Khadijah" : "0532335983", "Abdullah" : "0545341144","Rawan" : "0545534556" 
,"Faisal" : "0560664566", "Layla": "0567917077"}

def find_num(number):
    for name, phone in book_phone.items():
        if phone == number:
            return name
number = input("Enter a phone number:")
print(find_num(number))
if not number.isdigit() or len(number) != 10:
      print("This is invalid number")
elif number in book_phone:
  print("the owner is:"+ book_phone[number]+ "")
    
else:
   print("Sorry, the number is not found")




lst = [5,0,34,9,0,13,8]
def move_zero(lst):
    nonzero = [x for x in lst if x !=0]
    zero = [j for j in lst if j == 0]
    return nonzero + zero


