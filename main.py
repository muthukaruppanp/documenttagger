import os
dir_path = os.path.dirname(os.path.realpath(__file__))

inputfile = open(dir_path+'\input.txt', "r")
temp = ''
for line in inputfile:
    temp += ' '+line.rstrip('\n')
inputfile.close()
lookupfile = open(dir_path+'\lookup.txt', "r")
lookupfield = dict()
staringindex = dict()
endingindex = list()
for line in lookupfile:
    lf = line.split('=')
    lookupfield[lf[0]] = lf[1].rstrip('\n')
    try:
        staringindex[lf[0]] = temp.index(lf[0])+len(lf[0])+1
        endingindex.append(temp.index(lf[0])-1)
    except:
        continue
lookupfile.close()
sortedsi = sorted(staringindex.items(),key=lambda x:x[1])
endingindex.sort()
del endingindex[0]
endingindex.append(len(temp))

outputxml = open(dir_path+"\output.xml","w+")
outputxml.write('<mChart>\n')
for i in range(len(sortedsi)):
    outputxml.write('<{lookup}><header>{section}</header>{description}</{lookup}>\n'.format(lookup=lookupfield[sortedsi[i][0]],section=sortedsi[i][0],description=temp[sortedsi[i][1]:endingindex[i]]))

outputxml.write('</mChart>')
outputxml.close()
