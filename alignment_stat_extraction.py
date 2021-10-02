import os

# change the working directory to where the example files are located
os.chdir(os.path.realpath('examples'))
print(os.listdir())

# import 483510-hisat2-hybrid-alignment-trimmed.out as a list with the first 117 lines trimmed out
with open(os.path.join(os.getcwd(), '483510-hisat2-hybrid-alignment-trimmed.out'), 'r') as f:
    text = f.read().split("\n") # splitting each line and storing it as an element an a list
    text = text[118:] # the first 117 lines are junk

print(text[0:5])