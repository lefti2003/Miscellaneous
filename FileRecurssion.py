import os
import sys


def find_files(suffix, dirname):
    # create a list of file and sub directories
    # names in the given directory
    if os.path.isfile(dirname) and dirname.endswith(".c"):
        files = []
        files.append(dirname)
        return files
    elif os.path.exists(dirname):
        allfiles = os.listdir(dirname)
        files = []
        # Iterate over all the entries
        for entry in allfiles:
            # Create full path

            filepath = os.path.join(dirname, entry)
            if filepath.endswith(suffix):
                files.append(filepath)
            elif os.path.isdir(filepath):
                files = files + find_files(suffix, filepath)
        # If entry is a directory then get the list of files in this directory
    else:

        sys.exit(f"Directory {dirname} does not Exist. Try a valid directory!")

    return files

# Test 1
extension = '.c'
directory = './testdir'
listOfFiles1 = find_files(extension, directory)

for file_extc in listOfFiles1:
    print(file_extc)

#./testdir\subdir1\a.c
#./testdir\subdir3\subsubdir1\b.c
#./testdir\subdir5\a.c
#./testdir\t1.c

# Test 2

try:
    extension = '.c'
    directory = 'badtestdir'
    listOfFiles2 = find_files(extension, directory)

    for file_extc in listOfFiles2:
        print(file_extc)
except:
    print('An Exception occurred')
# Directory  does not Exist. Try a valid directory!

# Test 3

extension = '.d'
directory = './testdir'
listOfFiles3 = find_files(extension, directory)

if len(listOfFiles3) > 0:
    for file_extc in listOfFiles3:
        print(file_extc)
else:
    print('No such files found')

# No such files found

# Test 4
# Takes care of the case if the directory is a file

extension = '.c'
directory = './testdir/t1.c'
listOfFiles4 = find_files(extension, directory)

if len(listOfFiles4) > 0:
    for file_extc in listOfFiles4:
        print(file_extc)
else:
    print('No such files found')

# No such files found
