class student:
  def __init__(self, name, color, gpa, is_gay):
    self.name = name
    self.color = color
    self.gpa = gpa
    self.is_gay = is_gay
  
  def on_honor_roll(self):
    if self.gpa >= 3.5:
      return True
    else:
      return False





class Question:
  def __init__(self, prompt, answer):
    self.prompt = prompt
    self.answer = answer
