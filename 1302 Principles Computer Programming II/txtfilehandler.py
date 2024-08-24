import csv
import time


def chooseOption():
    print('--- --- --- Main Menu --- --- ---')
    option = input('Choose option:\n' \
         '[1] Create new text file\n' \
         '[2] Read text file content\n'
         '[3] Append to text file\n'
         '[4] Search text file\n' \
         '[5] Export to CSV\n' \
         '[6] Exit program\n'
         'option = ')

    return option


option = chooseOption()

while option != '6':

    if option == '1':  # Create
        name = input('What do you want to name the file?: ')

        try:
            f = open(name + '.txt', 'w')
            f.close()

        except:
            print('An error occurred during the CREATE operation!')

    elif option == '2':  # Read
        name = input('Which file would you like to read?: ')

        try:
            f = open(name + '.txt', 'r')
            content = f.read()
            print(content)
            f.close()

        except:
            print('An error occurred during the READ operation!')

    elif option == '3':  # Append
        name = input('What is the name of the file?: ')
        content = input('Type the content of the file you want added here: \n')

        try:
            f = open(name + '.txt', 'a')
            f.write(content)
            f.close()

        except:
            print('An error occurred during the APPEND operation')

    elif option == '4':  # Find
        name = input('What is the name of the file?: ')
        text = input('What is the text you would like to find?: ')

        try:
            f = open(name + '.txt', 'r')
            lines = f.readlines()

            x = 0

            for line in lines:

                if line.find(text) != -1:
                    print('Line number: ' + str((lines.index(line) + 1)))

                    x = 1

            if x == 0:
                print('No results')

        except:
            print('An error occurred during the FIND operation!')

    elif option == '5':  # Export
        name_file = input('What is the name of the text file: ')
        name_csv = input('What is the name of the csv file: ')

        try:
            with open(name_file + '.txt', 'r') as in_file:
                stripped = (line.strip() for line in in_file)
                lines = (line.split(",") for line in stripped if line)

                with open(name_csv + '.csv', 'w') as out_file:
                    writer = csv.writer(out_file)
                    writer.writerows(lines)

        except:
            print('An error occurred during the EXPORT operation!')

    else:
        print('Invalid option!')

    time.sleep(1.5)

    print('Going Back to main menu ', end='')

    for i in range(4):
        print('.', end='')
        time.sleep(.4)
        time.sleep(.4)
        
    print()
    option = chooseOption()
