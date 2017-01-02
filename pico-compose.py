import glob, sys, os
from shutil import copyfile

output = os.path.basename(os.path.dirname(os.path.realpath(__file__))) + '.p8'

# make a copy of the assets.p8 file to use as the base
copyfile('src/assets.p8', output)

filenames = glob.glob('src/*.p8')

with open(output, 'a') as outfile:
    for fname in filenames:
        if fname!='src/assets.p8':
            with open(fname, 'r') as readfile:
                outfile.write('\n' + readfile.read())