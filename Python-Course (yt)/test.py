from classTest import nig
from classTest import Question

array = ['324', 23, 43, 5]

for char in array:
  pass
  # print(char)

nig1 = nig('jamal', 'black', 1.1, True)

# print(nig1.gpa)

print(nig1.on_honor_roll())






question_promts = [
  'what is your color?\n(a)black\n(b)purple\n(c)yellow',
  'what color are your bannas?\n(a)black\n(b)white\n(c)yellow',
  'what is your name?\n(a)jamal\n(b)tom\n(c)bob'
]

questions = [
  Question(question_promts[0], "a"),
  Question(question_promts[1], "a"),
  Question(question_promts[2], "a")
]

def run(questions):
  score = 0
  for q in questions:
    answer = input(q.prompt)
    if answer == q.answer:
      score += 1
  print(f"you got {score}/{len(questions)} right")

# run(questions)