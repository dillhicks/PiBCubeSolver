import cv2
import movement as mv
import scan 
import kociemba 

if __name__ == "__main__":
	face1, face2 = scan.init_scan()
	mv.init_turn()
	face3, face4 = scan.init_scan()
	mv.init_turn()
	face5, face6 = scan.init_scan()
	mv.init_turn()

	