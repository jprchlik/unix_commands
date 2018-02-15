import os
import sys, getopt
import numpy as np
from scipy import misc

def main(argv):
    files = argv
    strlength = int(np.log10(len(files)))+1
    outformat = '{0:'+str(strlength)+'d}'
    
    for j,i in enumerate(files):
        img = misc.imread(i,flatten=0)
        badr,badg,badb, = np.where(img == 0)
        zrate = float(badr.size)/float(img.size)
        if zrate > 0.8:
            print 'Removing {0}, {1:4.2f}% zeros'.format(i,100.*zrate)
            os.remove(i)




if __name__=="__main__":
    main(sys.argv[1:])	

