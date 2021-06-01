class Ride:
  def __init__(self, fromCity, toCity, date, nSeats):
    self.fromCity = fromCity
    self.toCity = toCity
    self.date = date
    self.nSeats = nSeats
  def __str__(self):
    return "From: " + self.fromCity + ", To: " + self.toCity + ", Date: " + self.date + ", Seats: " + self.nSeats

rides = []

def createRide(fromCity, toCity, date, nSeats):
  rides.append(Ride(fromCity, toCity, date, nSeats))

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
      print("There is 1 ride stored" if len(rides) == 1 else "There are " + str(len(rides)) + " rides stored")
      for ride in rides:
        print(ride, end = '\n')
    elif split[0] == "C" and len(split) == 5:
      createRide(split[1], split[2], split[3], split[4])
    elif split[0] == "R" and len(split) == 2:
      raise NotImplementedError
    elif split[0] == "S":
      raise NotImplementedError
  print("Exiting...")

main()