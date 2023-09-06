'''
Implement Services, provided in lambda function.
Services Offered in this tools
1) Moorse Code
2) Temprature Converter
3) Password Strength Checker
4) Email Validator
5) String Capitalization
 '''
import re

# Python program to implement Morse Code Translator
# Dictionary representing the morse code chart
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
					'C':'-.-.', 'D':'-..', 'E':'.',
					'F':'..-.', 'G':'--.', 'H':'....',
					'I':'..', 'J':'.---', 'K':'-.-',
					'L':'.-..', 'M':'--', 'N':'-.',
					'O':'---', 'P':'.--.', 'Q':'--.-',
					'R':'.-.', 'S':'...', 'T':'-',
					'U':'..-', 'V':'...-', 'W':'.--',
					'X':'-..-', 'Y':'-.--', 'Z':'--..',
					'1':'.----', '2':'..---', '3':'...--',
					'4':'....-', '5':'.....', '6':'-....',
					'7':'--...', '8':'---..', '9':'----.',
					'0':'-----', ', ':'--..--', '.':'.-.-.-',
					'?':'..--..', '/':'-..-.', '-':'-....-',
					'(':'-.--.', ')':'-.--.-'}

# Function to encrypt the string
# according to the morse code chart

# 1
def encrypt(message : str) -> str:
    '''
    Encrypt message into moorse code.
    
    Parametrs
    --------
    message
		Text to converted into moorse code
    
	Return
    string
    '''
    cipher = ''
    for letter in message:
        if letter != ' ':
            # Looks up the dictionary and adds the
            # corresponding morse code
            # along with a space to separate
            # morse codes for different characters
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            cipher += ' '

    return cipher

# Function to decrypt the string
# from morse to english
# def decrypt(message : str) -> str:
#    '''
#     Encrypt message into moorse code.
    
#     Parametrs
#     --------
#     message
# 		Moorse code to converted into text
    
# 	Return
#     string
#     '''
# 	message += ' '
# 	decipher = ''
# 	citext = ''
# 	for letter in message:
# 		# checks for space
# 		if (letter != ' '):
# 			# counter to keep track of space
# 			i = 0
# 			# storing morse code of a single character
# 			citext += letter
# 		# in case of space
# 		else:
# 			# if i = 1 that indicates a new character
# 			i += 1
# 			# if i = 2 that indicates a new word
# 			if i == 2 :
# 				# adding space to separate words
# 				decipher += ' '
# 			else:
# 				# accessing the keys using their values (reverse of encryption)
# 				decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
# 				.values()).index(citext)]
# 				citext = ''
# 	return decipher

# 2
def temp_converter(to_temp : str , from_temp : str, temp : int ) -> float:
    '''
    Temprature conversion from farenheit to celsius and vice versa

    Parameters
    ---------- 
    
    Return
    ------
    
    '''
    if to_temp == 'F' and from_temp == 'C':
        temp_cal = (temp-32)/1.8
        return temp_cal
    if to_temp == 'C' and from_temp == 'F':
        temp_cal = (temp * 1.8)+32
        return temp_cal


# 3
def validate_password(password : str) -> bool:
    '''
    Check stregth of password
    
    Parameters
    ---------- 
    password
			Password to check strength 
    Return
    bool
    ------
    '''
    # Check if the password has at least 8 characters
    if len(password) < 8:
        return False
    # Check if the password contains at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return False
    # Check if the password contains at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return False
    # Check if the password contains at least one digit
    if not re.search(r'\d', password):
        return False
    # Check if the password contains at least one special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    # If all the conditions are met, the password is valid
    return True

# 4   
def validate_email(email : str) -> bool:  
    '''
    Validate the email using regular expression.
    
    Parameters
    ---------- 
    email
		Email to validate
    
    Return
    ------
		bool
     '''
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):  
         return True  
    return False  

# 5
def string_capitalization(name : str ) -> str:
    '''
     Capitalize first letter of word.
    Parameters
    ---------- 
    name
     Word to capitalize .
     
    Return
    ------
    string
      '''
    return name.capitalize()


# # Executes the main function
# if __name__ == '__main__':
#     main()
#     print(2, temp_converter("F","C",45))
#     print(3,validate_password("qwe2344!@@"))
#     print(4,validate_email("zain@gmail.com"))
#     print(5,string_capitalization("zzzain"))
