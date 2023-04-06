#
# lists all the files in the specified directory and subdirs
# only the files that have '.py' or '.c' extensions
#
import os

path = '.'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.py' in file or '.c' in file:
            files.append(os.path.join(r, file))

for f in files:
    print(f)


# alternative method using glob

#import glob
#folders = [f for f in glob.glob(path + "**/", recursive=True)]


