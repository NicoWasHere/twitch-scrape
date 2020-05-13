import sys

numOfChars = 4
inputFile = ""
outputFile = "output.txt"


if len(sys.argv) == 1:
    print("NO FILE INCLUDED")
    exit()

if sys.argv[1] == "-h" or sys.argv[1] == "-help":
    print("This script allows you to iterate through a word list and only keeps words of a specific size\nIf a size is not specified, it will default to 4 characters. You can also add an output file as the second arguement.\nusage. python3 parse_file.py [input file] [output file (optional)] [number of characters] ")
    exit()

try:
    open(sys.argv[1]).close()
    inputFile = sys.argv[1]
except:
    print("FILE NOT FOUND")
    exit()

if len(sys.argv)>2 and not sys.argv[2].isnumeric():
    outputFile = sys.argv[2]
elif len(sys.argv)>2 and sys.argv[2].isnumeric():
    numOfChars = int(sys.argv[2])

if len(sys.argv)>3:
    if not sys.argv[3].isnumeric():
        print("NOT A NUMBER")
        exit()
    numOfChars = int(sys.argv[3])

words = open(inputFile,'r')
result = open(outputFile,'w')
for line in words.readlines():
    line = line.strip('\n')
    if(len(line) == numOfChars and line.isalnum()):
        result.write(line.lower()+'\n')
print("SUCCESS")
words.close()
result.close()