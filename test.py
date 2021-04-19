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
        startingHand(line)
    elif "ending hand" in line:
        endingHand(line)
    elif "Flop" in line:
        flop(line)
    elif "Turn" in line:
        turn(line)
    elif "River" in line:
        river(line)
    
    #Pre Hand Actions
    elif "Player stacks" in line:
        print("PLAYER STACKS BY HAND")
    elif "Your hand is" in line:
        yourHand(line)
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


#-- starting hand #2  (No Limit Texas Hold'em) (dealer: "bb @ THAVWp2FAr") --
def startingHand(line):
    #print("In starting hand")
    #print(line)
    handNum = line.split(" ")[3].split("#")[1]
    #print(handNum)
    gameType = line.split(")")[0].split("(")[1]
    #print(gameType)
    dealer = line.split(")")[1].split("(")[1].split("\"")[1]
    #print(dealer)
    dealerName = dealer.split(" ")[0]
    #print(dealerName)

#-- ending hand #1 --
def endingHand(line):
    #print("In ending hand")
    #print(line)
    handNum = line.split(" ")[3].split("#")[1]
    #print(handNum)

#Flop:  [3?, 8?, 7?]
def flop(line):
    #print("In flop")
    #print(line)
    cards = line.split("]")[0].split("[")[1].split(", ")
    #print(cards)

#Turn: 3?, 8?, 7? [3?]
def turn(line):
    #print("In turn")
    #print(line)
    turnCard = line.split("]")[0].split("[")[1]
    #print(turnCard)
    card = Card(turnCard)
    card.myfunc()

#River: 3?, 8?, 7?, 3? [4?]
def river(line):
    #print("In river")
    #print(line)
    riverCard = line.split("]")[0].split("[")[1]
    #print(riverCard)

#Your hand is Qâ™ , 3â™
def yourHand(line):
    #print("in your hand")
    #print(line)
    cardOne = line.split(" ")[3].split(",")[0]
    #print(cardOne)
    cardTwo = line.split(" ")[4]
    #print(cardTwo)
    card = Card(cardOne)
    card.myfunc()
    card = Card(cardTwo)
    card.myfunc()


class Card:
  def __init__(self, cardString):
    print(cardString)
    number = cardString[0:1]
    if "10" in cardString:
        number = "T"

    suit = "error"
    if "â™£" in cardString:
        suit = "c"
    elif "â™¦" in cardString:
        suit = "d"
    elif "â™¥" in cardString:
        suit = "h"
    elif "â™" in cardString:
        suit = "s"

    self.number = number #2-9,T,J,Q,K,A
    self.suit = suit #h,d,c,s

  def myfunc(self):
    print(self.number,self.suit)




def main():
    print("Main function")
    readCSV('./GameData/pokersimple.csv')

if __name__ == "__main__":
    main()