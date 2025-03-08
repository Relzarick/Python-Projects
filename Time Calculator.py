day_of_the_week = ['monday', "tuesday", "wednesday", "thursday", "friday", "saturday", 'sunday']
def add_time(start, duration, date = ""):
  #? Start from 0 to -2||Start from -2 to -1
  time = start[:-2]
  meridiem = start[-2:].lower()
  date = date.lower()
  day_counter = 0

  hours = int(''.join(i for i in time if i != ':'))
  time_elapsed = int(''.join(i for i in duration if i != ':'))

 
  while time_elapsed != 0: 
    #* This calc remaining time
    if time_elapsed < 1200:
      hours += time_elapsed

      if hours >= 1200:
        meridiem = 'pm' if meridiem == 'am' else 'am'
        day_counter += 1 if meridiem == 'am' else 0 
        hours -= 1200
      time_elapsed = 0  

    if time_elapsed >= 1200:
      hours += 1200
      time_elapsed -= 1200

      if hours >= 1200:
        meridiem = 'pm' if meridiem == 'am' else 'am'
        day_counter += 1 if meridiem == 'am' else 0 
        hours -= 1200


  hour = int(str(hours)[:-2])
  minutes = int(str(hours)[-2:])
  
  while int(minutes) >= 60:
    minutes -= 60
    hour += 1
    
  if minutes < 10:
    minutes = f'0{str(minutes)}'
  if hour == 12:
    meridiem = 'pm' if meridiem == 'am' else 'am'
    day_counter += 1 if meridiem == 'am' else 0 

  #* This is for 12 O'clock timmings
  formated_time = f'{hour}:{minutes} {meridiem.upper()}' if hour else f'12:{minutes} {meridiem.upper()}'

  
  if date:
    start_index = day_of_the_week.index(date)
    #* Index = the remainder||Seven is the number of days in a week 
    end_index = (start_index + day_counter) % 7
    day = day_of_the_week[end_index].capitalize()

    if day_counter:
      formated_counter = f'{day} (next day)' if day_counter == 1 else f'{day} ({day_counter} days later)'
      return f'{formated_time}, {formated_counter}'
    else:
      return f'{formated_time}, {day}'
  #* returns below if no date input
  else:
    if day_counter:
      formated_counter = '(next day)' if day_counter == 1 else f'({day_counter} days later)'
      return f'{formated_time} {formated_counter}'
    else:
      return f'{formated_time}'
      
 
print(add_time('12:00 PM', '1:00'))

