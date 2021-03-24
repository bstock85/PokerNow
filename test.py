import csv

def readCSV():
    with open('./GameData/pokersimple.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            print(row)
            line_count += 1
        print(f'Processed {line_count} lines.')


def main():
    print("Main function")
    readCSV()

if __name__ == "__main__":
    main()