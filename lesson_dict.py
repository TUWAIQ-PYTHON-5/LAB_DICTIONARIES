# LAB_DICTIONARIES


## Q1:Build a phone book program that receives the phone number (Use Input to let the user provide the number), and returns the name of the owner. 
#You can follow the table below:

#| Name    | Number      |
#| -------- | ---------- |
#| Amal     | 0568323222 |
#| Mohammed | 0522222232 |
#| Khadijah | 0532335983 |
#| Abdullah  | 0545341144 |
#| Rawan    | 0545534556 |
#| Faisal   | 0560664566 |
#| Layla    | 0567917077 |


#- If the number exists, print the owner. Otherwise, print "Sorry, the number is not found".
#- If the number is less or more than 10 numbers, print "This is invalid number".
#- If the number contains letters or symbols, print "This is invalid number".

phone_book = {
"0568323222" : "Amal",
"0522222232" : "Mohammed"
,"0532335983" : "Khadijah"
, "0545341144" : "Abdullah"
,"0545534556" : "Rawan"
,"0560664566" : "Faisal"
,"0567917077" : "Layla"}
print(phone_book)

user_quistion = input("Please enter the phone number you need to search : ")
git_num = user_quistion


if len(git_num) != 10 and git_num != git_num.isdigit :
    print ("This is invalid number")
else :
    print("Welcome ",phone_book.get(git_num, "Sorry, the number is not found"))

## Q2:Write a function that receives a list containing the following numbers : 
#- [5, 0, 34, 9, 0, 13, 8]
#- rearranges the list so that the zeros are the end of the list, and finally returns the arranged list.

def sort_num (numbers : list) :
    numbers.sort(reverse=True)
    return numbers

print(sort_num([5, 0, 34, 9, 0, 13, 8]))
