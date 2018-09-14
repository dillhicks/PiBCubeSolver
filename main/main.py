import cv2
import movement as mv
import scan 
import kociemba 

cube = []

def get_Orientation(face):
	if face[1][1] == 'W':
        cube[0] = face;
    else if face[1][1] == 'G':
        cube[1] = face;
    else if face[1][1] == 'O':
        cube[2] = face;
    else if face[1][1] == 'B':
        cube[3] = face;
    else if face[1][1] == 'R':
        cube[4] = face;
    else if face[1][1] == 'Y':
        cube[5] = face;

if __name__ == "__main__":
	f1, f2 = scan.init_scan()
	mv.init_turn()
	f3, f4 = scan.init_scan()
	mv.init_turn()
	f5, f6 = scan.init_scan()
	mv.init_turn()
	get_Orientation(f1)
	get_Orientation(f2)
	get_Orientation(f3)
	get_Orientation(f4)
	get_Orientation(f5)
	get_Orientation(f6)




