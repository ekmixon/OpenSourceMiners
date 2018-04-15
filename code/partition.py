import pandas as pd
import sys, os, re

def miniturize(fname):
    fpath = "data/" + fname
    # Open the file to be cleaned
    if(os.path.isfile(fpath)):
        f = pd.read_csv(fpath, low_memory=False)
    else:
        print("ERROR: %s is an invalid file path" % fpath)
        exit(1)
    
    mini = f.iloc[::100, :]
    mini.to_csv
    

# Get all of the paths to the data
paths = [f for f in os.listdir("./data/") if re.match(r".*\.csv", f)]

root_path = "data/"
for path in paths:
    print("Miniturizing %s" % path)
    miniturize(root_path + path)