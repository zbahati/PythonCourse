name = input("What's your name? ")

match name:
  case 'Bahati'|'Bah'|'Bran':
    print("B house")
  case 'Reno':
    print("R house")
  case _:
    print("Who?")
