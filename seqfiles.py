import os
import sys, getopt
from glob import glob
import numpy as np

def main(argv):
    files = glob(argv)
    strlength = int(np.log10(len(files)))+1
    outformat = '{0:'+str(strlength)+'d}'
    
    for j,i in enumerate(files):
        reg = []
        reg.append( i.split('.')[0])
        reg.append( 'seq'+outformat.format(j).replace(' ','0'))
        print 'Renaming {0} to {1}'.format(i,i.replace(reg[0],reg[1]))
        os.rename(i,i.replace(reg[0],reg[1]))




if __name__=="__main__":
    main(sys.argv[1:])	
