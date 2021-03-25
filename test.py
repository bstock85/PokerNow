import csv

def readCSV(filename):
    print("Read CSV")
    data = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        fields = next(csv_reader)
        print("headers ",fields)

        for row in csv_reader:
            data.append(row)

        del data[0]
        data.reverse()
        for row in data:
            #print(row[0])
            processLine(row[0])
            line_count += 1
        print(f'Processed {line_count} lines.')

"""
Determine the type of line
TODO: create a function on useful lines to handle the information
    replace print statements with returns for useless lines
"""
def processLine(line):
    #Hand lines
    if "starting hand" in line:
        print("STARTING HAND")
    elif "ending hand" in line:
        print("ENDING HAND")
    elif "Flop" in line:
        print("FLOP")
    elif "Turn" in line:
        print("TURN")
    elif "River" in line:
        print("RIVER")
    
    #Pre Hand Actions
    elif "Player stacks" in line:
        print("PLAYER STACKS BY HAND")
    elif "Your hand is" in line:
        print("PLAYER HAND")
    elif "posts a small blind" in line:
        print("SMALL BLIND")
    elif "posts a big blind" in line:
        print("BIG BLIND")

    #Player actions
    elif "bets" in line:
        print("PLAYER BETS")
    elif "calls" in line:
        print("PLAYER CALLS")
    elif "checks" in line:
        print("PLAYER CHECKS")
    elif "folds" in line:
        print("PLAYER FOLDS")
    elif "raises to" in line:
        print("PLAYER RAISES")

    #Run it twice
    elif "run it twice" in line:
        print("RUN IT TWICE")

    #Post Hand Actions
    elif "returned" in line:
        print("BET RETURNED")
    elif "collected" in line:
        print("POT COLLECTED")
    elif "shows" in line:
        print("PLAYER SHOWS HAND")
    elif "Undealt cards" in line:
        print("UNDEALT CARDS")

    #Admin related lines
    elif "requested a seat." in line:
        print("REQUEST SEAT")
    elif "The admin approved the player" in line:
        print("APPROVED SEAT")
    elif "joined the game with a stack of" in line:
        print("STARTING STACK SIZE")
    elif "spectator mode" in line:
        print("SPECTATOR MODE")
    elif "quits" in line:
        print("QUITS GAME")
    elif "stand up" in line:
        print("LEAVES SEAT")
    elif "blind was changed" in line:
        print("BLIND CHANGED")
    elif "the admin queued the stack change" in line:
        print("STACK CHANGE")
    elif "the admin updated the player" in line:
        print("UPDATED PLAYER")
    
    #Error unknown line
    else:
        print("Unknown line: ", line)

def main():
    print("Main function")
    readCSV('./GameData/poker2_15.csv')

if __name__ == "__main__":
    main()