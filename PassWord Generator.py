from secrets import choice
from string import ascii_letters, ascii_uppercase, digits, punctuation
from time import sleep
import re

class PasswordGenerator:
  def prompt(self):
    print('\nWelcome to the Secure Password Generator!\n')
    
    while True:
      sleep(.4)
      print('Choose an option to proceed:')
      print('1. Express Mode - Automatically generate a password with default settings and a randomly chosen length')
      print('2. Custom Mode - Specify your password length and customize the character composition\n')

      userchoice = input('Enter 1 for Express Mode or 2 for Custom Input Mode: ')

      if userchoice == "1":
        sleep(.3)
        print("\nYou selected Express Mode. Generating password...\n")
        sleep(.5)
        print(f"Here is your secure password: {self._generator_express()}\n")
        break
      elif userchoice == "2":
        sleep(.3)
        print("\nYou have selected Custom Mode. Let's customize your password.")
        self._prompt_custom()
        break
      else:
          sleep(.5)
          print("\nThat was an invalid option.\n")
          
      
  def _generator_express(self):
    str_length = choice(range(10, 17))
    random_chara = ascii_letters + digits + punctuation

    num_re = r'\d'
    letter_re = r'[A-Z]'

    while True:
      random_str = ''.join(choice(random_chara) for _ in range(str_length))
      
      # * Appends missing characters
      if not re.search(num_re, random_str):
        random_str += ''.join(choice(digits) for _ in range(4))
      if not re.search(letter_re, random_str):
        random_str += ''.join(choice(ascii_uppercase) for _ in range(4))

      random_str = ''.join(choice(random_str) for _ in range(str_length))

      has_num = re.search(num_re, random_str)
      has_cap = re.search(letter_re, random_str)

      if has_num and has_cap:
        break

    return random_str

  def _generator_custom(self, length, ambi, adv):
    print(length)
    print(ambi)
    print(adv)

  def _prompt_custom(self):
    user_length = self._prompt_length()
    sleep(.3)
    ambi = self._prompt_ambi()
    sleep(.3)
    adv_settings = self._prompt_comp()
        
    print(f"Here is your secure password: {self._generator_custom(user_length, ambi, adv_settings)}\n")

  def _prompt_length(self):
    while True:
      try:
        user_length = int(input('\nEnter desired password length (8-25): '))
        if user_length in range(8, 26):
          return user_length
        else:
          sleep(.3)
          print("\nInvalid input. Please enter a number between 8 and 25.")
      except ValueError:
        sleep(.3)
        print("\nInvalid input. Please enter a valid number.")


  def _prompt_ambi(self):
    print("\nAmbiguous characters are sometimes hard to distinguish, such as: (e.g., “O”, “0”, “l”, “1”)\n")
    while True:
      query = input('\nWould you like to exclude these ambiguous characters? (Y or N): ').strip().lower()
      if query in ['yes', 'no', 'y', 'n']:
        return query
      else:
        sleep(.3)
        print('\nInvalid input. Please enter Yes or No.')
  

  def _prompt_comp(self):
    print("\nBy default, the password will include the following:")
    print("1. One uppercase letter")
    print("2. One lowercase letter")
    print("3. One digit")
    print("4. One special character\n")
    while True:
      adv_settings = input("\nWould you like to also customize these settings? (Y or N): ").strip().lower()
      if adv_settings in ['yes', 'no', 'y', 'n']:
        return adv_settings
      else:
        sleep(.3)
        print('\nInvalid input. Please enter Yes or No.')
  



if __name__ == '__main__':
  main = PasswordGenerator()
  # main.prompt()
  # main._generator_custom(13, 'yes', 'n')
 

# ! Dual mode 
# ! Utilize Python's secrets module 

# ? one for custom input length one express
# * If a user enters a non-int, negative number, 
# * or a number outside range (less than 8 or greater than 25)
# app should display an error message and prompt for valid input.

# When a valid input is provided, the process should move to the next step. (prompt again)
# When random mode is selected, the app must choose a length within the predefined secure bounds.
# Validate that the generated password’s length is within those bounds.
# ? generate passwords for user to choose

# ? only allow settings if advanced mode
# By default, one uppercase letter and lowercase letter, one digit, and one special character.
# let user opt out ambiguous charas (e.g., “O”, “0”, “l”, “1”)


# t (optional) save generated passwords to a file. 
# ? this file must be encrypted (using Python’s cryptography library)
