# “All vanity plates must start with at least two letters.”
# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
# “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
# “No periods, spaces, or punctuation marks are allowed.”
# Assume that any letters in the user’s input will be uppercase. 

# #initial plan
# 2 <= len(string) <= 6
# slice the list [0:2] and check whether first two are letters or not
# use in statement to check whether there are punctuation and spaces
# check endwith method to check whether number is in end 

def main():
    plate = input("Plate: ")
    if is_valid(plate): #is_valid going to return bool value
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if length_check(s) and  first_2_letter_check(s) and end_is_number_check(s) and no_punctuation_space_check(s):
        return True
    else:
        return False


def length_check(plate):
    if 2 <= len(plate) <= 6:
        return True
    else:
        return False

def first_2_letter_check(plate):

    first_2_letter = plate[0:2]

    if not first_2_letter.isdecimal(): #checks whether it's not numeric character 
        return True
    else:
        return False
    
def no_punctuation_space_check(plate):

    check = True
    punctuation = ["!", "#", "$", "%", "&" , "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";" ,"<" , "=", ">", "?", "@", "[", "]", "^", "`", "{", "|" ,"}", "~",'"'," "]
    for i in plate:
        if i in punctuation:
            check = False
            
    if check: return True
    else: return False

def end_is_number_check(plate):
    # iterate plate 
    # check whether there is number
    # if then check whether it's in last

    number = False

    for i in plate: # Checks whether there is number in inputed plate number
        if i.isdecimal(): 
            number = True 

    if number: # Check whether number == True
        if plate.endswith(tuple(f"{i}" for i in range(10))): # makes list 0 to 9 and then convert that list to tuple. endswith(tuple) is to check whether there is number at the end
            return True
        else: 
            return False
        
    else:
        return True





main()