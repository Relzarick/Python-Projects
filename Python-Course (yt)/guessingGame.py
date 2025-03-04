secret_word = 'giraffe'
guess = ''
attempts = 0
attempt_limit = 3

while guess != secret_word:
  if attempts < attempt_limit:
    guess = input('Enter guess: ')
    attempts += 1
  else:
    print('You ran out of guesses')
    break
  
if guess == secret_word:
  print('You guessed it!')