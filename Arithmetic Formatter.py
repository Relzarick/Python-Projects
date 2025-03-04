import re

def arithmetic_arranger(problems, show_answers=False):
  #* Checks for non digits and ^+-
  matches = re.findall(r"[^\d\s\[\]\"',+-]", str(problems)) 
  
  
  if len(problems) > 5:
    return 'Error: Too many problems.'
  
  if matches:
    # print(matches)
    if re.findall('[a-zA-Z]', str(matches)):
      return 'Error: Numbers must only contain digits.'
    else:
      return "Error: Operator must be '+' or '-'."
    
  #? Expresion||Iterate outer loop||If any var(num) matches condition >= 10000||Iterate inner loop||Returns inv NUMBER
  result = ['Error: Numbers cannot be more than four digits.' for i in problems if any(float(num) >= 10000 for num in re.findall(r'\d+', i))]
  if result:
    return result

  answer = 0
  
  for problem in problems:
    num1 = float(problem.split(' ')[0])
    operator = problem.split(' ')[1]
    num2 = float(problem.split(' ')[2])

    if operator == '+':
      answer = num1 + num2
    else:
      answer = num1 - num2

    

  

  # return problems
print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')



  #! OLD CODE (replaced with list comprehension)
  # for i in problems:
  #   numbers = re.findall(r'\d+', i)
  #   # print(numbers)
  #   for num in numbers:
  #     if float(num) >= 10000:
  #       return 'Error: Numbers cannot be more than four digits.'