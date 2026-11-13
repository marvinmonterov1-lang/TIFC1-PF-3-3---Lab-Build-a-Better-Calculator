def main():
  print("Hello learners!")

def addmultiplenumbers(numbers):
  total = 0
  for number in numbers:
    total += number
  return total


def multiplymultiplenumbers(numbers):
  total = 1
  for number in numbers:
    total *= number
  return total


def isiteven(num):
  if num % 2 == 0:
    return True
  else:
    return False


def isitaninteger(num):
  if num % 1 == 0:
    return True
  else:
    return False





if __name__ == "__main__":
  main()


