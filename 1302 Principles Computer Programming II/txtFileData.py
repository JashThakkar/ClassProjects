file = input('file input: ')
num_words = 0
line_count = 0

output_file = open(input('file output: '), 'w')

with open(file, 'r') as f:
    lines = len(f.readlines())
    output_file.write('Total Number of lines:'+ str(lines))

with open(file, 'r') as f:
    for line in f:
        words = line.split()
        num_words += len(words)
    output_file.write('\nTotal number of words: ' + str(num_words))

num_words = 0

with open(file, 'r') as f:
    for line in f:
        words = line.split()
        num_words += len(words)
        output_file.write('\nLine '+str(line_count+1)+ ' >> '+str(num_words)+' words')
        num_words = 0
        line_count = line_count + 1

output_file.close()

# This program takes an inpute of a .txt file and outputs another .txt file that had data about the inputed .txt file
