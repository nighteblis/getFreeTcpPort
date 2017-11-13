#!/usr/bin/python3.5

import subprocess
import numpy as np

############################
#
###########################

#port check range
portrange=[10000,65535]

#the count we want to get unsed  listen ports with tcp protocol
getPortCount=4


exitcode,output=subprocess.getstatusoutput('netstat -ln | grep tcp | awk \'{print $4}\' | rev | cut -d \':\' -f 1 | rev');

#print(exitcode)
#print(output)


usedports=output.split('\n')
portCounter=1
usedportsdic={}
newports=[]

for usedport in usedports:
    usedportsdic[usedport]=1

getPortCount=4
portCounter=1

for porti in range(portrange[0],portrange[1]):
    if(str(porti) in usedportsdic):
        print(" used: "+str(porti))
    else:
        if(portCounter>getPortCount):
            break
        newports.append(porti)
        portCounter+=1
#    print(porti)


print(newports)


