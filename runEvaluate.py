import pylab
import matplotlib.pyplot as plt
import math
plt.style.use('ggplot')

file = open("bin/mtcnnDiscROC.txt")
plt.figure("DiscRoc")
plt.xlabel("False Positive")
plt.ylabel("True Positive Rate")
#plt.grid()

listX=[]
listY=[]
listLeg=[]
for line in file:
    #name = line.split()
    #for pointName in name:
        #points_file = open(pointName)
        #for point in points_file:
    xy = line.split()
    if (float(xy[1]) < 8000):
        listX.append(int(xy[1]))
        listY.append(xy[0])

plt.plot(listX,listY)
plt.ylim(ymin=0, ymax=1)

plt.grid(b=True, which='major', color='k', linestyle='-')
plt.grid(b=True, which='minor', color='k', linestyle='-', alpha=0.2)
plt.minorticks_on()
plt.savefig('fddb.png')
plt.show()

#listY=[]
#listX=[]
#listLeg.append( pointName[0:len(pointName)-6])
#plt.legend(listLeg, prop={'size':9})
#listLeg=[]



#======================================


#file = open("mtcnnContROC.txt")
#plt.figure("ContRoc")
#plt.xlabel("False Positive Per Frame")
#plt.ylabel("True Positive Rate")
#plt.grid()


#for line in file:
    #name = line.split()
    #for pointName in name:
        #listLeg.append(pointName[0:len(pointName)-6])
        #points_file = open(pointName)
        #for point in points_file:
            #xy = point.split()

            #if (float(xy[1]) < 3000):
                #listX.append(int(xy[1])/float(2844))
                #listY.append(xy[0])

        #plt.plot(listX,listY)
        #listY=[]
        #listX=[]
#plt.legend(listLeg,prop={'size':10})

#plt.show()

