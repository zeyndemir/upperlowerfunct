#purpose: The function that changes strings like the below sentence

#before : "hi my name is john and i am learning python"
#after : Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN"


#range() : this function gives us the oppurtunity of a number between two values.

def alternating(string):
    new_string =""
    #browse the indexes of the entered string
    for string_index in range(len(string)):
        # if the index is an even number turn it into an upper letter
        if string_index % 2 == 0:
            new_string += string[string_index].upper()
        # if the index is an odd number turn it into a lower letter
        else :
            new_string += string[string_index].lower()

        print(new_string)