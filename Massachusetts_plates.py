def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if letters_characters(s):
      return True
    else:
        return False

def letters_characters(word):
    #Check the max-length is 6 and min-length is 2
    if not (len(word)<=6 and len(word)>=2):
        return False
    #Check the first 2 numbers are letters
    if not word[:2].isalpha():
        return False
    #Check if the the word is alphnumeric
    if not word.isalnum():
        return False
        
def valid_num(word):
    if word[-1:len(word)].isnumeric():
        return False
    return True


main()
