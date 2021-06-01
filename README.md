# Rides
A Python program that allows the user to create and search for rides between cities

## Usage

### Download
- `git clone https://github.com/codingbiro/simplefactoring.git`

### Run
- *Requires python 3*
- `python3 app.py`

### Commands
- List all rides: `ls`
- Quit program: `q`
- Create a new ride from from-city to to-city on date with number-of-seats available for booking: `C from-city to-city date number-of-seats`
- Create a return-trip on date using the last created ride as a template: `R date`
- Search for rides between cities in the specified date range with the specified number of seats available. All parameters are optional. Please see examples below for some combinations: `S [from-city [to-city]] [from-date [to-date]] [minimum-free-seats]`