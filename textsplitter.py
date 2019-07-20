import argparse
import math
import os 
import sys


# when creating txt make sure to use utf-8

UPPERWORDBOUND = 24000

parser = argparse.ArgumentParser(description='Splits a textfile')
parser.add_argument('filename')
args = parser.parse_args()
input_file = open(sys.argv[1])
print(input_file)

f = open(input_file.name, "r", encoding="utf-8")
fileContent = f.read()

output_file_name = os.path.splitext(input_file.name)[0]

totalwordCount = len(fileContent.split())
finaltextfileamount = totalwordCount / UPPERWORDBOUND
finaltextfileamount = math.ceil(finaltextfileamount)
allowed_words_per_file =  math.ceil(totalwordCount / finaltextfileamount)

print("words = " + str(totalwordCount))
print("final parts amount = " + str(finaltextfileamount)) 
print("allowed word per file = " + str(allowed_words_per_file)) 


file_word_counter = 0
smallfile = None
firstfile = True
filecounter = 0

with open(input_file.name, "r", encoding="utf-8") as bigfile:
    for lineno, line in enumerate(bigfile):
        line_word_counter = len(line.split())

        # if the file would be to big or the word counter is zero and there havent been files before
        if file_word_counter > allowed_words_per_file or firstfile == True:
            # if the file exists close it
            if smallfile:
                smallfile.close()
            # create a new file
            filecounter = filecounter + 1  
            small_filename = output_file_name + "_part" + str(filecounter) + ".txt"
            smallfile = open(small_filename, "w", encoding="utf-8")
            firstfile = False 
            file_word_counter = 0
        #write the line to the new file
        smallfile.write(line)
        file_word_counter = file_word_counter + line_word_counter
    # close the last file 
    if smallfile:
        smallfile.close()
        

