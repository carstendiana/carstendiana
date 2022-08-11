import os
from glob import glob
path = "C:\Users\Excis\Desktop\csv_file"
filenames = [y for x in os.walk(path)
             for y in glob(os.path.join(x[0], '*.csv'))]
# get the Path of all files in sub directories and save them in a list
print(len(filenames))

with open(path+'_allcsv', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
