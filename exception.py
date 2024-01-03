def get_values():
  number = int(input("What's your age? "))
  print(f" I'm {number} years old")

try:
  get_values()

except ValueError:
  print('age is not valid number')
