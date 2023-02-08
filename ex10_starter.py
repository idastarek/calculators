import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(hdir,'*')

# TODO: Use the glob.glob() function to obtain the list of filenames

files = glob.glob(pattern)
print(files)

# TODO: use os.path.getsize to find each file's size
for item in files:
    sizes = os.path.getsize(item)
 #   if sizes != 0:
  #      print(sizes)
   #     else:
    if sizes == 0:
        files.remove(item)

    else:
        new_name = os.path.basename(item)
        print(new_name, sizes)



# size = os.path.getsize(pattern)
# print(size)

# TODO: Add a test to only display files that are not zero length



# TODO: Remove the leading directory name(s) from each filename before you print it -
# using os.path.basename()

