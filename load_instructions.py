words = []
for x in range(32):
    words.append(0)

    # Create an iterator to chop off the first record of the truth table    
    # iter = itertools.islice(sys.stdin, 1, None)

    # # Open the truth table csv file
    # csv_reader = csv.DictReader(iter)

    # # Process logic table rows
    # for row in csv_reader:
    #     print(row)

    # df = pd.read_csv('tt.csv')

    # for row in df.itertuples():

    #     # print(type(row.ibin))
    #     x = str(row.ibin)
    #     y = str(row.obin)
    #     words[(int(x,2))] = int(y, 2)


i = 0
with open('instruction_memory.txt', 'r') as file:
    # Read each line in the file
    for line in file:
        # Print each line
        words[i] = int(line.strip(),16)
        i = i+1

# for word in words:
#     print(word)

f = open("instruction.rom", "w")
f.write("v3.0 hex words addressed\n")

row_value = 0
for x in range(int(32/8)):
    line = ""
    line += f"{row_value:0>2x}: "
    for y in range(8):
        line += f"{words[(x*4)+y]:0>8x} "
        row_value += 1
    line = line[:-1]
    line += "\n"
    f.write(line)
    
# # Need to write words in 8 byte rows, hex formatted row_value = 0
# for x in range(int(32/8)):
#     line = ""
#     line += f"{row_value:0>32x}: "
#     for y in range(8):
#         line += f"{words[(x*8) + y]:0>32x} "
#         row_value = row_value+1
#     line = line[:-1]
#     line += "\n"
#     f.write(line)