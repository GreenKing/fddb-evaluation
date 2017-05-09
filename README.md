fddb-evaluation for Windows
===========================

### Dependency and Tools
- OpenCV
- CMake
- Python

### Usage  

**Build**  
run the following command:
```
git clone https://github.com/GreenKing/fddb-evaluation
# ${fddb-evaluation}
cd fddb-evaluation/fddb-evaluation 
mkdir build
cd build
cmake .. -G"Visual Studio 12 2013 Win64"
```
Open `fddb-eval.sln` file to compile `fddbEval.exe`. It should be noticed that it doesn't work with `release` mode in my computer. So you should be very careful if you use the `release` mode.

After building the runable file,
```
cd ${fddb-evaluation}
cp fddb-evaluation/DEBUG/fddbEval.exe bin/
```

**fddbEval usage**
```
./fddbEval [OPTIONS]
   -h              : print usage
   -a fileName     : file with face annotations (default: ellipseList.txt)
   -d fileName     : file with detections (default: faceList.txt)
   -f format       : representation of faces in the detection file (default: 0)
                     [ 0 (rectangle), 1 (ellipse), or  2 (pixels) ]
   -i dirName      : directory where the original images are stored 
		     (default: ~/scratch/Data/facesInTheWild/)
   -l fileName     : file with list of images to be evaluated (default: temp.txt)
   -r fileName     : prefix for files to store the ROC curves (default: temp)
   -s              : display the matching detection-annotation pairs.
   -z imageFormat  : image format used for reading images for the annotation set 
                     (default: .jpg )
```

for example
```
eval -a ./FDDB-folds/FDDB-fold-ellipseList.txt -d  ./fddb.txt -i path/to/images/dir -l ./FDDB-folds/FDDB-folds.txt -r ./facedet
```

**Evaluation**
```
cd ${fddb-evaluation}
python runEvaluate.py
```