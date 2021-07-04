def arithmetic_arranger(problems, option = False):
  n = len(problems)
  i = 0
  line1 = ''
  line2 = ''
  line3 = ''
  line4 = ''
  if(n > 5):
    return "Error: Too many problems."
  else:
    # if(option is True):
    for arithmetic in problems:
      i+=1
      space = '    '
      if i == n:
        space = ''
      arg = arithmetic.split()
      if arg[1] != '+' and arg[1] != '-':
        return "Error: Operator must be '+' or '-'."
      else:
        Num1 = arg[0]
        Num2 = arg[2]
        width = max(len(Num1),len(Num2)) + 2
        # print(width)
        if Num1.isdecimal() and Num2.isdecimal():
          num1 = int(Num1)
          num2 = int(Num2)
          if num1 < 10000 and num2 < 10000:
            line1 = line1 + ''.rjust(width - len(Num1)) + Num1 + space
            line2 = line2 + arg[1] + ''.rjust(width - len(Num2) - 1) + Num2 + space
            line3 = line3 + ''.rjust(width,'-') + space
            result = 0
            if arg[1] == '+':
              result = str(num1 + num2)
            else:
              result = str(num1 - num2)
            line4 = line4 + ''.rjust(width - len(result)) + result + space
          else:
            return "Error: Numbers cannot be more than four digits."
        else:
          return "Error: Numbers must only contain digits."
  arranged_problems = line1 + '\n' + line2 + '\n' + line3
  if(option is True):
    arranged_problems = arranged_problems + '\n' +line4

  return arranged_problems