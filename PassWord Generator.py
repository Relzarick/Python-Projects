from secrets import choice
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from time import sleep
import re
import os

class PasswordGenerator:
  def __init__(self):
    self.random_char = ascii_lowercase + ascii_uppercase + digits + punctuation
    self.user_length = None

    self.terminal_width = os.get_terminal_size().columns

    self.num_re = r'\d'
    self.letter_re = r'[A-Z]'
    self.ambi_re = r'[o0i1]'
    
    self.options = ['yes', 'no', 'y', 'n']
    self.ambiguous = ['o', '0', 'i', '1']

    self.user_yes = ['yes', 'y']
    self.user_no = ['no', 'n']

  def prompt(self):
    print(f"\n{'Welcome to the Secure Password Generator!'.center(self.terminal_width)}\n")
    
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

    while True:
      random_str = ''.join(choice(self.random_char) for _ in range(str_length))
      
      # * Appends missing characters
      if not re.search(self.num_re, random_str):
        random_str += ''.join(choice(digits) for _ in range(4))
      if not re.search(self.letter_re, random_str):
        random_str += ''.join(choice(ascii_uppercase) for _ in range(4))

      random_str = ''.join(choice(random_str) for _ in range(str_length))

      # ! check if i have to add the last parem
      if self.validate_password(random_str, False, False):
        return random_str

  def _generator_custom(self, length, ambi, adv):
    random_str = ''.join(choice(self.random_char) for _ in range(length))
    user_config, (upper_case, lower_case, digits_num, special_char) = adv
    
    ambi_config = False
    adv_config = False
    
    if ambi in self.options and ambi in self.user_yes:
      ambi_config = True
      random_str = ''.join(choice(self.random_char) if i in self.ambiguous else i for i in random_str)
      
    if user_config in self.options and user_config in self.user_yes:
      adv_config = True

      while True:
        # t this will keep looping until all the requirements are met before breaking
        break
      
      if self.validate_password(random_str, ambi_config, adv_config, adv):
        return random_str
    
  def validate_password(self, random_str, ambi_enabled, adv_enabled, adv_settings):

    has_num = re.search(self.num_re, random_str)
    has_cap = re.search(self.letter_re, random_str)
    has_ambi = re.search(self.ambi_re, random_str)

    if not has_num and has_cap:
      return False
    
    if ambi_enabled:
      if has_ambi:
        return False
      
    if adv_enabled:
      _, (req_upper, req_lower, req_digits, req_special) = adv_settings

      total_upper = sum(1 for c in random_str if c in ascii_uppercase)
      total_lower = sum(1 for c in random_str if c in ascii_uppercase)
      total_digits = sum(1 for c in random_str if c in digits) 
      total_special = sum(1 for c in random_str if c in punctuation)

      # * Total must at least reach the specified minimum requirements. 
      if total_upper < req_upper or total_lower < req_lower or total_digits < req_digits or total_special < req_special:
        return False

    return True
    

  def _prompt_custom(self):
    self.user_length = self._prompt_length()
    sleep(.3)
    ambi = self._prompt_ambi()
    sleep(.3)
    user_config = self._prompt_composition()

    print(f"Here is your secure password: {self._generator_custom(self.user_length, ambi, user_config)}\n")

  def _prompt_length(self):
    while True:
      try:
        user_length = int(input('\nEnter desired password length (10-25): '))
        if user_length in range(10, 26):
          return user_length
        else:
          sleep(.3)
          print("\nInvalid input. Please enter a number between 10 and 25.")
      except ValueError:
        sleep(.3)
        print("\nInvalid input. Please enter a valid number.")


  def _prompt_ambi(self):
    print("\nAmbiguous characters are sometimes hard to distinguish, such as: (e.g. “O”, “0”, “l”, “1”)\n")
    while True:
      query = input('\nWould you like to exclude these ambiguous characters? (Y or N): ').strip().lower()

      if query in self.options:
        return query
      else:
        sleep(.3)
        print('\nInvalid input. Please enter Yes or No.')
  

  def _prompt_composition(self):
    print("\nBy default, the password will include at least the following:")
    print("1. One uppercase letter")
    print("2. One lowercase letter")
    print("3. One digit")
    print("4. One special character\n")
    while True:
      
      user_config = input("\nWould you like to also customize these settings? (Y or N): ").strip().lower()

      if user_config in self.options:

        if user_config in self.user_yes:
          return user_config, self._adv_config()
        
        return user_config, (1, 1, 1, 1)
      else:
        sleep(.3)
        print('\nInvalid input. Please enter Yes or No.')
  

  def _adv_config(self):
    while True:
      upper_case = int(input("\nEnter the minimun number of uppercase letters to include: "))
      lower_case = int(input("Enter the minimum number of lowercase letters to include: "))
      digits = int(input("Enter the minimum number of digits to include: "))
      special_char = int(input("Enter the minimum number of special characters to include: "))

      total_char = upper_case + lower_case + digits + special_char

      if total_char < self.user_length:
        return upper_case, lower_case, digits, special_char
      else:
        print(f'\nYou have exceeded your desired password length.\n')
  


if __name__ == '__main__':
  main = PasswordGenerator()
  # main.prompt()
  main._prompt_custom()
  

 

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
