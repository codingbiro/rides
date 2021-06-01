class Ride:
  def __init__(self, fromCity, toCity, date, nSeats):
    self.fromCity = fromCity
    self.toCity = toCity
    self.date = date
    self.nSeats = nSeats
  def __str__(self):
    return "From: " + self.fromCity + ", To: " + self.toCity + ", Date: " + self.date + ", Seats: " + self.nSeats

rides = []

def printRides(elements):
  print("There is 1 ride stored" if len(elements) == 1 else "There are " + str(len(elements)) + " rides stored")
  for element in elements:
    print(element)

def createRide(fromCity, toCity, date, nSeats):
  rides.append(Ride(fromCity, toCity, date, nSeats))

def createReturnRide(date):
  fromRide = rides[len(rides) - 1]
  rides.append(Ride(fromRide.toCity, fromRide.fromCity, date, fromRide.nSeats))

def search(fromCity = "", toCity = "", fromDate = "", toDate = "", minFreeSeats = ""):
  results = []
  for ride in rides:
    cityCondition = (not bool(fromCity) or ride.fromCity == fromCity) and (not bool(toCity) or ride.toCity == toCity)
    dateCondition = (not bool(fromDate) or ride.date >= fromDate) and (not bool(toDate) or ride.date <= toDate)
    if (not bool(toDate)):
      dateCondition = not bool(fromDate) or ride.date == fromDate
    freeSeatsCondition = not bool(minFreeSeats) or ride.nSeats >= minFreeSeats
    if cityCondition and dateCondition and freeSeatsCondition:
      results.append(ride)
  printRides(results)

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
    splitCommand = command.split()
    if command == "q":
      exit = True
    elif command == "ls":
      printRides(rides)
    elif splitCommand[0] == "C" and len(splitCommand) == 5:
      createRide(splitCommand[1], splitCommand[2], splitCommand[3], splitCommand[4])
    elif splitCommand[0] == "R" and len(splitCommand) == 2:
      createReturnRide(splitCommand[1])
    elif splitCommand[0] == "S" and len(splitCommand) == 2:
      search(splitCommand[1])
    elif splitCommand[0] == "S" and len(splitCommand) == 3:
      search(splitCommand[1], splitCommand[2])
    elif splitCommand[0] == "S" and len(splitCommand) == 4:
      search(splitCommand[1], splitCommand[2], splitCommand[3])
    elif splitCommand[0] == "S" and len(splitCommand) == 5:
      search(splitCommand[1], splitCommand[2], splitCommand[3], splitCommand[4])
    elif splitCommand[0] == "S" and len(splitCommand) == 6:
      search(splitCommand[1], splitCommand[2], splitCommand[3], splitCommand[4], splitCommand[5])
    elif splitCommand[0] == "S" and len(splitCommand) == 7:
      search(splitCommand[1], splitCommand[2], splitCommand[3], splitCommand[4], splitCommand[5], splitCommand[6])
  print("Exiting...")

main()