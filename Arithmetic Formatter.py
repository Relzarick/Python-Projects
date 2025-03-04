import re

def arithmetic_arranger(problems, show_answers=False):
  if len(problems) > 5:
    return 'Error: Too many problems.'
  
  #* Checks for non digits and ^+-
  matches = re.findall(r"[^\d\s\[\]\"',+-]", str(problems)) 

  #? If ^match returns None||Else execute if block
  if matches:
    print(matches)
    if re.findall('[a-zA-Z]', str(matches)):
      return 'Error: Numbers must only contain digits.'
    else:
      return "Error: Operator must be '+' or '-'."

  #? Expresion||Iterate outer loop||If any var(num) matches condition >= 10000||Iterate inner loop||Returns inv NUMBER
  result = ['Error: Numbers cannot be more than four digits.' for i in problems if any(float(num) >= 10000 for num in re.findall(r'\d+', i))]
  if result:
    return result
  
  line1 = ''
  line2 = ''
  lines = ''
  answers = ''
  format = ''

  for problem in problems:
    num1 = problem.split(' ')[0]
    operator = problem.split(' ')[1]
    num2 = problem.split(' ')[2]

    #* rjust() only works on str
    if operator == '+':
      sum = str(int(num1) + int(num2))
    else:
      sum = str(int(num1) - int(num2))
    # print(sum)

    #* rjust() is inclusive of str
    length = max(len(num1), len(num2)) + 2
    print(length)
    top = str(num1).rjust(length)
    #* -1 here because of +2 prior (THIS IS FOR THE SPACING BETWEEN OPERATOR)
    bottom = operator + str(num2).rjust(length - 1)
    dashes = ''
    answer = sum.rjust(length)
    for _ in range(length):
      dashes += "-"

    #? This indents if its not the last calc
    if problem != problems[-1]:
      line1 += top + '    '
      line2 += bottom + '    '
      lines += dashes + '    '
      answers += answer + '    '
    else:
      line1 += top
      line2 += bottom
      lines += dashes
      answers += answer

  if show_answers:
    format = f'{line1}\n{line2}\n{lines}\n{answers}'
  else:
    format = f'{line1}\n{line2}\n{lines}'
  return format


    
print(f'\n{arithmetic_arranger(["24 + 8521", "3801 - 2", "45 + 43", "123 + 49"], True)}')



  #! OLD CODE (replaced with list comprehension)
  # for i in problems:
  #   numbers = re.findall(r'\d+', i)
  #   # print(numbers)
  #   for num in numbers:
  #     if float(num) >= 10000:
  #       return 'Error: Numbers cannot be more than four digits.'