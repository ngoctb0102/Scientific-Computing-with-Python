def add_time(start, duration, optional = ''):
  new_time = ''
  clForm = ''
  numDayAfter = ''
  weekDay = ''
  newStrMinute = ''

  start = start.split()
  startTime = start[0].split(':')
  s_hour = int(startTime[0])
  if start[1] == 'PM':
    s_hour += + 12
  s_minute = int(startTime[1])

  duration = duration.split(':')
  d_hour = int(duration[0])
  d_minute = int(duration[1])

  newHour = s_hour + d_hour
  newMinute = s_minute + d_minute

  if newMinute > 59:
    newHour += 1
    newMinute = newMinute % 60
  if newMinute < 10:
    newStrMinute += '0' + str(newMinute)
  else:
    newStrMinute += str(newMinute)
  
  timeStep = int(newHour / 12)
  newHour = newHour % 12
  if newHour == 0:
    newHour += 12

  timeJump = int(timeStep/2)

  if timeStep % 2 == 0:
    clForm += ' AM'
  else:
    clForm += ' PM'

  if timeJump == 1:
    numDayAfter += ' (next day)'
  elif timeJump > 1:
    numDayAfter += ' (' + str(timeJump) + ' days later)'
  
  week = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
  lowerWeek = [day.lower() for day in week]
  optional = optional.lower()
  count = 0
  if optional in lowerWeek:
    for day in lowerWeek:
      if optional == day:
        break
      else:
        count+=1
    weekDay += ', ' + week[(count + timeJump) % 7]

  new_time = str(newHour) + ':' + newStrMinute + clForm + weekDay + numDayAfter


  return new_time