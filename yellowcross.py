import faceRotation
def turnalgo():
	rotateFront()
	rotateCCTop()
	rotateRight()
	rotateTop()
	rotateCCRight()
	rotateCCFront()

def yellowCross():
	count = 0
	for i in irange(1, 3):
		for j in jrange(1, 3):
			if i = 2 and j = 2
				continue
			if top[i][j] != "y"
				count++
	#if only the center is yellow
	if count = 8
		turnalgo()
	#finding the side of the fish
	if top[1][2] == "y" and top[2][1] == "y"
		turnalgo()
		turnalgo()
		return true
	if top[1][2] == "y" and top[2][3] == "y"
		rotateTop()
		turnalgo()
		turnalgo()
		return true
	if top[2][3] == "y" and top[3][2] == "y"
		rotateTop()
		rotateTop()
		turnalgo()
		turnalgo()
		return true
	if top[2][1] == "y" and top[3][2] == "y"
		rotateCCTop()
		turnalgo()
		turnalgo()
		return true
	#if there is three yellows in a row 
	if top[2][1] == "y" and top[2][3] == "y"
		turnalgo()
		return true
	if top[1][2] == "y" and top[3][2] == "y"
		rotateTop()
		turnalgo()
		return true
yellowCross()






