def main():
  print("Rides by Vince Biro")
  print("Commands:")
  print("ls - list rides")
  print("q - exit")
  print("C fromCity toCity date nSeats - create a ride")
  print("R date - create a return-ride for last created ride")
  print("S [from-city [to-city]] [from-date [to-date]] [minimum-free-seats] - search for rides")
  exit = False
  while not exit:
    command = input("Your command: ")
    split = command.split()
    if command == "q":
      exit = True
    elif command == "ls":
      raise NotImplementedError
    elif split[0] == "C" and len(split) == 5:
      raise NotImplementedError
    elif split[0] == "R" and len(split) == 2:
      raise NotImplementedError
    elif split[0] == "S":
      raise NotImplementedError
  print("Exiting...")

main()