import csv
import sys

def usage():
    print("Usage: parse_ntds.py -c|-nt inputfile")
    sys.exit(1)

if len(sys.argv) != 3:
    usage()

option = sys.argv[1]
inputfile = sys.argv[2]

if not inputfile.endswith('.txt'):
    print("Input file must be a .txt file")
    sys.exit(1)

try:
    with open(inputfile, 'r') as f:
        lines = f.readlines()
except FileNotFoundError:
    print("Input file not found!")
    sys.exit(1)

if option == '-c':
    with open('output.csv', 'w', newline='') as csvfile:
        fieldnames = ['Username', 'RID', 'LM Hash', 'NT Hash']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for line in lines:
            parts = line.strip().split(':')
            writer.writerow({'Username': parts[0], 'RID': parts[1], 'LM Hash': parts[2], 'NT Hash': parts[3]})
    print("CSV file created: output.csv")
elif option == '-nt':
    for line in lines:
        parts = line.strip().split(':')
        print(f"{parts[0]},{parts[3]}")
else:
    usage()
