import os
import sys, getopt

def main(argv):
   reg = argv[0].split('/')
   files = argv[1:]
   
   for i in files:
       print 'Renaming {0} to {1}'.format(i,i.replace(reg[1],reg[2]))
       os.rename(i,i.replace(reg[1],reg[2]))




if __name__=="__main__":
    main(sys.argv[1:])	
