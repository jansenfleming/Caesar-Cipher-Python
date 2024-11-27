message ="JANSEN FLEMING"
shift = 7

last_char_code = 90
char_range = 26
first_char_code = 65

def caesar_shift(message, shift):
    
     #result placeholder
    result ="" 


    #Go through each of the letters in the message
    for char in message.upper( ):
        if char.isalpha():

        #convert each letter to the ASCII Code
            char_code = ord(char)

            new_char_code = char_code + shift

            if new_char_code > last_char_code: 
                new_char_code = new_char_code - char_range

            if new_char_code < first_char_code:
                new_char_code = new_char_code + char_range

            new_char = chr(new_char_code)

            result = result + new_char 
            
        else:
            result = result + char
    
    
    print(result)

user_message = input("Message to encrypt:")
user_shift_key = int(input("Shift Key (Integer)"))
caesar_shift(user_message, user_shift_key)  
