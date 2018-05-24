import faceRotation


def bluepiece():
    #if piece is on the bottom layer
        #blue face
    if left[3][2] == "b" and bottom[2][1] == "w":
        return true
    if left[3][2] == "w" and bottom[2][1] == "b":
        rotateCCLeft()
        rotateCCFront()
        rotateCCBottom()
        return true
        #red face
    if front[3][2] == "b" and bottom[1][2] == "w":
        rotateCCBottom()
    if front[3][2] == "b" and bottom[1][2] == "w":
        rotateFront()
        rotateLeft()
        return true
        #green face
    if right[3][2] == "b" and bottom[2][3] == "w":
        rotateBottom()
        rotateBottom()
        return true
    if right[3][2] == "w" and bottom[2][3] == "b":
        rotateCCRight()
        rotateFront()
        rotateCCBottom()
        return true
        #orange face
    if back[1][2] == "b" and bottom[3][2] == "w":
        rotateBottom()
        return true
    if back[1][2] == "w" and bottom[3][2] == "b":
        rotateBottom()
        rotateCCLeft()
        rotateCCFront()
        rotateCCBottom()
        return true
            
    #if piece is on the second layer
    if left[2][3] == "b" and front[2][1] == "w":
        rotateLeft()
        return true
    if left[2][3] == "w" and front[2][1] == "b":
        rotateCCFront()
        rotateCCBottom()
        return true
    if front[2][3] == "b" and right[2][1] == "w":
        rotateRight()
        rotateCCBottom()
        return true
    if front[2][3] == "w" and right[2][1] == "b":
        rotateFront()
        rotateCCBottom()
        return true
    if back[2][1] == "b" and left[2][1] == "w":
        rotateCCBack()
        rotateBottom()
        return true
    if back[2][1] == "w" and left[2][1] == "b":
        rotateCCLeft()
        return true
    if right[2][3] == "b" and back[2][3] == "w":
        rotateRight()
        rotateBottom()
        rotateBottom()
        return true
    if right[2][3] == "w" and back[2][3] == "b":   
        rotateBack()
        rotateBottom() 
        return true

    #if piece is in top layer
    if top[1][2] == "w" and back[3][2] == "b":
        rotateCCTop()
        rotateLeft()
        rotateLeft()
        return true
    if top[2][1] == "w" and left[1][2] == "b":
        rotateLeft()
        rotateLeft()
        return true
    if top[3][2] == "w" and front[1][2] == "b":
        rotateTop()
        rotateLeft()
        rotateLeft()
        return true
    if top[2][3] == "w" and right[1][2] == "b":
        rotateTop()
        rotateTop()
        rotateLeft()
        rotateLeft()
        return true
        #second orientation
    if top[1][2] == "b" and back[3][2] == "w":
        rotateCCBack()
        rotateCCLeft()
        return true
    if top[2][1] == "b" and left[1][2] == "w":
        rotateCCTop()
        rotateCCBack()
        rotateCCLeft()
    if top[3][2] == "b" and front[1][2] == "w":
        rotateCCTop()
        rotateCCTop()
        rotateCCBack()
        rotateCCLeft()
    if top[2][3] == "b" and right[1][2] == "w":
        rotateCCFront()
        rotateLeft()

bluepiece()

def redpiece()
    #if the piece is at the bottom layer
        #red face
    if front[3][2] == "r" and bottom[1][2] == "w":
        return true
    if front[3][2] == "w" and bottom[1][2] == "r":
        rotateCCFront()
        rotateRight()
        rotateCCTop()
        rotateFront()
        rotateFront()
        return true
        #green face
    if left[3][2] == "r" and bottom[2][3] == "w":
        rotateRight()
        rotateRight()
        rotateCCTop()
        rotateFront()
        rotateFront()
        return true
    if left[3][2] == "w" and bottom[2][3] == "r":
        rotateRight()
        rotateCCFront()
        return true
        #orange face
    if back[1][2] == "r" and bottom[3][2] == "w":
        rotateCCBack()
        rotateCCBack()
        rotateTop()
        rotateTop()
        rotateFront()
        rotateFront()
        return true
    if back[1][2] == "w" and bottom[3][2] == "r":
        rotateCCBack()
        rotateRight()
        rotateRight()
        rotateCCTop()
        rotateCCFront()
        rotateCCFRont()
        return true
    #if in second layer
    if front[2][1] == "r" and left[2][3] == "w":
        rotateCCFront()
        return true
    if front[2][1] == "w" and left[2][3] == "r":
        rotateLeft()
        rotateTop()
        rotateFront()
        rotateFront()
        return true
    if front[2][3] == "r" and right[2][1] == "w":
        rotateFront()
        return true
    if front[2][3] == "w" and right[2][1] == "r":
        rotateRight()
        rotateCCTop()
        rotateFront()
        rotateFront()
        return true
    if back[2][1] == "r" and left[2][1] == "w":
        rotateBack()
        rotateTop()
        rotateCCRight()
        rotateFront()
        return true
    if back[2][1] == "w" and left[2][1] == "r":
        rotateBack()
        rotateTop()
        rotateTop()
        rotateFront()
        rotateFront()
        return true
    if back[2][3] == "r" and right[2][3] == "w":
        rotateRight()
        rotateRight()
        rotateFront()
        return true
    if back[2][3] == "w" and right[2][3] == "r":
        rotateRight()
        rotateCCTop()
        rotateFront()
        rotateFront()
        return true
    #if in top layer
    if front[1][2] == "r" and top[3][2] == "w":
        rotateFront()
        rotateFront()
        return true
    if front[1][2] == "w" and top[3][2] == "r":
        rotateTop()
        rotateRight()
        rotateFront()
        return true
    if top[2][1] == "w" and left[1][2] == "r":
        rotateTop()
        rotateFront()
        rotateFront()
        return true
    if top[2][1] == "r" and left[1][2] == "w":
        rotateTop()
        rotateTop()
        rotateRight()
        rotateFront()
        return true
    if top[1][2] == "w" and back[3][2] == "r":
        rotateTop()
        rotateTop()
        rotateFront()
        rotateFront()
        return true
    if top[1][2] == "r" and back[3][2] == "w":
        rotateFront()
        rotateRight()
        rotateFront()
        return true
    if top[2][3] == "w" and right[1][2] == "r":
        rotateCCTop()
        rotateFront()
        rotateFront()
        return true
    if top[2][3] == "r" and right[1][2] == "w":
        rotateRight()
        rotateFront()
        return true
redpiece()

def orangepiece()
    #if at bottom layer
    if back[1][2] == "o" and bottom[3][2] == "w":
        return true
    if back[1][2] == "w" and bottom[3][2] == "o":
        rotateCCBack()
        rotateRight()
        rotateTop()
        rotateBack()
        rotateBack()
        return true
    if right[3][2] == "o" and bottom[2][3] == "w":
        rotateRight()
        rotateRight()
        rotateTop()
        rotateBack()
        rotateBack()
        return true
    if right[3][2] == "o" and bottom[2][3] == "w":
        rotateCCRight()
        rotateBack()
        return true
    #if second layer
    if front[2][1] == "o" and left[2][3] == "w":
        rotateRight()
        rotateRight()
        rotateBack()
        return true
    if front[2][1] == "w" and left[2][3] == "o":
        rotateRight()
        rotateTop()
        rotateBack()
        rotateBack()
        return true
    if front[2][3] == "o" and right[2][1] == "w":
        rotateLeft()
        rotateCCTop()
        rotateCCTop()
        rotateCCLeft()
        rotateRight()
        rotateBack()
        return true
    if front[2][3] == "w" and right[2][1] == "o":
        rotateLeft()
        rotateCCTop()
        rotateBack()
        rotateBack()
        return true
    if back[2][1] == "o" and left[2][1] == "w":
        rotateCCBack()
        return true
    if back[2][1] == "w" and left[2][1] == "o":
        rotateCCRight()
        rotateTop()
        rotateBack()
        rotateBack()
        return true
    if back[2][3] == "o" and right[2][3] == "w":
        rotateBack()
        return true
    if back[2][3] == "w" and right[2][3] == "o":
        rotateCCRight()
        rotateTop()
        rotateBack()
        rotateBack()
        return true
    #if top layer
    if front[1][2] == "o" and top[3][2] == "w":
        rotateTop()
        rotateTop()
        rotateBack()
        rotateBack()
        return true
    if front[1][2] == "w" and top[3][2] == "o":
        rotateTop()
        rotateRight()
        rotateBack()
        return true
    if top[2][1] == "w" and left[1][2] == "r":
        rotateTop()
        rotateTop()
        rotateRight()
        rotateBack()
        return true
    if top[2][1] == "o" and left[1][2] == "w":
        rotateRight()
        rotateBack()
        return true
    if top[1][2] == "w" and back[3][2] == "o":
        rotateBack()
        rotateBack()
        return true
    if top[1][2] == "o" and back[3][2] == "w":
        rotateTop()
        rotateRight()
        rotateBack()
        return true
    if top[2][3] == "w" and right[1][2] == "o":
        rotateTop()
        rotateBack()
        rotateBack()
        return true
    if top[2][3] == "o" and right[1][2] == "w":
        rotateTop()
        rotateTop()
        rotateRight()
        rotateBack()
        return true

orangepiece()

def greenpiece()
    #if bottom layer
    if bottom[2][3] == "w" and left[3][2] == "g":
        return true
    if bottom[2][3] == "g" and left[3][2] == "w":
        rotateRight()
        rotateCCFront()
        rotateTop()
        rotateFront()
        rotateCCRight()
        return true
    #if second layer
    if front[2][1] == "g" and left[2][3] == "w":
        rotateCCFront()
        rotateTop()
        rotateFront()
        rotateRight()
        rotateRight()
        return true
    if front[2][1] == "w" and left[2][3] == "g":
        rotateCCLeft()
        rotateTop()
        rotateTop()
        rotateLeft()
        rotateRight()
        rotateRight()
        return true
    if front[2][3] == "g" and right[2][1] == "w":
        rotateRight()
        rotateTop()
        rotateBack()
        rotateRight()
        rotateCCBack()
        return true
    if front[2][3] == "w" and right[2][1] == "g":
        rotateCCRight()
        return true
    if back[2][1] == "g" and left[2][1] == "w":
        rotateBack()
        rotateCCTop()
        rotateRight()
        rotateRight()
        rotateCCBack()
        return true
    if back[2][1] == "w" and left[2][1] == "g":
        rotateLeft()
        rotateTop()
        rotateTop()
        rotateCCLeft()
        rotateRight()
        rotateRight()
        return true
    if back[2][3] == "g" and right[2][3] == "w":
        rotateBack()
        rotateCCTop()
        rotateRight()
        rotateRight()
        rotateCCBack()
        return true
    if back[2][3] == "w" and right[2][3] == "g":
        rotateRight()
        return true
    #if top layer
    if front[1][2] == "g" and top[3][2] == "w":
        rotateTop()
        rotateRight()
        rotateRight()
        return true
    if front[1][2] == "w" and top[3][2] == "g":
        rotateFront()
        rotateCCRight()
        rotateCCFront()
        return true
    if top[2][1] == "w" and left[1][2] == "g":
        rotateTop()
        rotateTop()
        rotateRight()
        rotateRight()
        return true
    if top[2][1] == "g" and left[1][2] == "w":
        rotateTop()
        rotateFront()
        rotateCCRight()
        rotateCCFront()
        return true
    if top[1][2] == "w" and back[3][2] == "g":
        rotateCCTop()
        rotateRight()
        rotateRight()
        return true
    if top[1][2] == "g" and back[3][2] == "w":
        rotateBack()
        rotateRight()
        rotateRight()
        rotateCCBack()
        return true
    if top[2][3] == "w" and right[1][2] == "g":
        rotateRight()
        rotateRight()
        return true
    if top[2][3] == "g" and right[1][2] == "w":
        rotateCCTop()
        rotateFront()
        rotateCCRight()
        rotateCCFront()
        return true












    
