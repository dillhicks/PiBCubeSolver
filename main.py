import numpy as np
import printFaces as pf
import faceRotation as fr
import secondLayer as sl


#pf.printFace(fr.front)
#pf.printFace(fr.back)
#pf.printFace(fr.left)
#pf.printFace(fr.right)
#pf.printFace(fr.top)
#pf.printFace(fr.bottom)


pf.printFaces(fr.cube1)
print "\n"
sl.topLayerAlign(fr.cube1);
sl.secondLayerComplete(fr.cube1);

#sl.solveSecondLayer(fr.cube1)
print "\n"
pf.printFaces(fr.cube1)
