import matplotlib.pyplot as plt
import os
import fire

plt.style.use('ggplot')



class Evaluation(object):
    def eval(self, isdisc, name):
        test_type = "Disc" if isdisc else "Cont"
        roc_file = name + test_type + "ROC.txt"
        file = open(os.path.join("bin/", roc_file))
        plt.figure("DiscRoc")
        plt.xlabel("False Positive")
        plt.ylabel("True Positive Rate")

        listX=[]
        listY=[]
        listLeg=[]
        for line in file:
            xy = line.split()            
            listX.append(float(xy[1]))
            listY.append(float(xy[0]))
            
        plt.plot(listX,listY)
        plt.ylim(ymin=0, ymax=1)        
        plt.grid(b=True, which='major', color='k', linestyle='-')
        plt.grid(b=True, which='minor', color='k', linestyle='-', alpha=0.2)
        plt.minorticks_on()
        plt.savefig('fddb.png')
        plt.show()        


if __name__ == "__main__":
    fire.Fire(Evaluation)
    