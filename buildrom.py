import sys
import itertools
import csv
import pandas as pd

if __name__ == '__main__':
    words = []

    # Create a 512 list (9 bits) mapping to 9 bits of control data signals
    for x in range(512):
        words.append(0)

    # Create an iterator to chop off the first record of the truth table    
    # iter = itertools.islice(sys.stdin, 1, None)

    # # Open the truth table csv file
    # csv_reader = csv.DictReader(iter)

    # # Process logic table rows
    # for row in csv_reader:
    #     print(row)

    df = pd.read_csv('tt.csv')

    for row in df.itertuples():
        words[(int(row.ihex,16))] = int(row.ohex, 16)
    
    f = open("logic.rom", "w")
    f.write("v3.0 hex words addressed\n")
    
    # Need to write words in 16 byte rows, hex formatted
    row_value = 0
    for x in range(int(512/16)):
        line = ""
        line += f"{row_value:0>3x}: "
        for y in range(16):
            line += f"{words[(x*16) + y]:0>3x} "
            row_value = row_value+1
        line = line[:-1]
        line += "\n"
        f.write(line)
    


