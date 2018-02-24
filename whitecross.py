def bluepiece( blue[3][3], orange[3][3], green[3][3], red[3][3], yellow[3][3], white[3][3] ):
    #if piece is on the bottom layer
    for i in 3:
        if blue[3][i] == "b":
            for j in 3:
                if yellow[j][1] == "w":
                    #turn Fi twice
                    return true
        if orange[3][i] == "b"and yellow[1][i] == "w":
            #turn Di once, turn Fi twice
            return true
        if green[3][i] == "b":
            for j in 3:
                    #turn Di twice, turn Fi twice
                    return true
        if red[3][i] == "b" and yellow[3][i] == "w":
            #turn D once, turn Fi twice
            
    #if piece is on the second layer
    if blue[2][1] == "b" and red[2][3] == "w":
        #turn F once
        return true
    if blue[2][1] == "w" and red[2][3] == "b":
        #turn Li once, Ui once
        return true
    
    if blue[2][3] == "b" and orange[2][1] == "w":
        #turn Fi once
        return true
    if blue[2][3] == "w" and orange[2][1] == "b":
        #turn R once, U one
        return true
    
    if green[2][1] == "b" and orange[2][3] == "w":
        #turn B once, U twice
        return true
    if green[2][1] == "w" and orange[2][3] == "b":
        #turn Ri once, U once
        return true
    
    if green[2][3] == "b" and red[2][1] == "w":
        #turn L once, Ui once
        return true
    if green[2][3] == "b" and red[2][1] == "w":
        #turn Bi once, U twice
        return true
    
    #if piece is in top layer
    for i in 3 and j in 3:
        if white[i][j] == "w":
            if blue[1][2] == "b":
                return true
            if orange[1][2] == "b":
                #turn U once
                return true
            if green[1][2] == "b":
                #turn U twice
                return true
            if red[1][2] == "b":
                #turn Ui once
                return true

def orangepiece( blue[3][3], orange[3][3], green[3][3], red[3][3], yellow[3][3], white[3][3] )
    #if piece is in bottom layer
    for i in 3:
        if orange[3][i] == "o"and yellow[1][i] == "w":
            #turn R twice
            return true
        if blue[3][i] == "o":
            for j in 3:
                if yellow[j][1] == "w":
                    #turn D once, R twice
                    return true
        if green[3][i] == "o":
            for j in 3:
                    #turn B once, turn Ri once
                    return true
        if red[3][i] == "o" and yellow[3][i] == "w":`
            #turn Di once, turn R twice
    
    #if piece is on the second layer
    if blue[2][1] == "o" and red[2][3] == "w":
        #turn F once, D once, Fi once, R three times
        return true
    if blue[2][1] == "w" and red[2][3] == "o":
        #turn R once
        return true
    
    if blue[2][3] == "o" and orange[2][1] == "w":
        #turn L once, D twice, R twice
        return true
    if blue[2][3] == "w" and orange[2][1] == "o":
        #turn Li twice, Di twice, R once
        return true
    
    if green[2][1] == "o" and orange[2][3] == "w":
        #turn B once, U twice
        return true
    if green[2][1] == "w" and orange[2][3] == "o":
        #turn Ri once, U once
        return true
    
    if green[2][3] == "w" and red[2][1] == "o":
        #turn L once, Ui once
        return true
    if green[2][3] == "o" and red[2][1] == "w":
        #turn Bi once, U twice
        return true
                
    #if piece is in top layer
    for i in 3 and j in 3:
        if white[i][j] == "w":
            if orange[1][2] == "o":
                return true
            if green[1][2] == "o":
                #turn B twice, Di once, R twice
                return true
            if red[1][2] == "b":
                #turn Li twice, D twice, R twice
                return true

def greenpiece( blue[3][3], orange[3][3], green[3][3], red[3][3], yellow[3][3], white[3][3] )
    #if piece is in the bottom layer
     for i in 3:
        if green[3][i] == "g" and yellow[1][i] == "w":
            #turn B twice
            return true
        if orange[3][i] == "g" and yellow[1][i] == "w":
            #turn D once, B twice
            return true
        if blue[3][i] == "g" and yellow[i][1] == "w":
            #turn D twice, turn B twice
            return true
        if red[3][i] == "g" and yellow[i][3]:`
            #turn Di once, turn R twice
            return true
        
    #second layer
    if blue[2][1] == "g" and red[2][3] == "w":
        #Fi once, Di twice, F once, B twice
        return true
    if blue[2][1] == "w" and red[2][3] == "g":
        #turn L once, Di once, Li once, B twice
        return true
    if blue[2][3] == "g" and orange[2][1] == "w":
        #turn F twice, D twice, Fi once, B twice
        return true
    if blue[2][3] == "w" and orange[2][1] == "g":
        #turn Ri once, D once, R once, B twice
        return true
    if green[2][1] == "g" and orange[2][3] == "w":
        #turn Bi once
        return true
    if green[2][1] == "w" and orange[2][3] == "g":
        #turn R once, D once, Ri once, B twice
        return true
    if green[2][3] == "w" and red[2][1] == "g":
        #turn L once, Di once, Li once, B twice
        return true
    if green[2][3] == "g" and red[2][1] == "w":
        #turn B once
        return true
    
    #if piece is in top layer
    for i in 3 and j in 3:
        if white[i][j] == "w":
            if green[1][2] == "g":
                return true
            if red[1][2] == "g":
                #turn Li twice, Di twice, B twice
                return true
def redpiece( blue[3][3], orange[3][3], green[3][3], red[3][3], yellow[3][3], white[3][3] )
    #if piece is in bottom layer
    for i in 3:
        if orange[3][i] == "o"and yellow[1][i] == "w":
            #turn L twice
            return true
        if blue[3][i] == "o":
            for j in 3:
                if yellow[j][1] == "w":
                    #turn D once, R twice
                    return true
        if green[3][i] == "o":
            for j in 3:
                    #turn B once, turn Ri once
                    return true
        if red[3][i] == "o" and yellow[3][i] == "w":`
            #turn Di once, turn R twice
    
    #if piece is on the second layer
    if blue[2][1] == "o" and red[2][3] == "w":
        #turn F once, D once, Fi once, R three times
        return true
    if blue[2][1] == "w" and red[2][3] == "o":
        #turn R once
        return true
    
    if blue[2][3] == "o" and orange[2][1] == "w":
        #turn L once, D twice, R twice
        return true
    if blue[2][3] == "w" and orange[2][1] == "o":
        #turn Li twice, Di twice, R once
        return true
    
    if green[2][1] == "o" and orange[2][3] == "w":
        #turn B once, U twice
        return true
    if green[2][1] == "w" and orange[2][3] == "o":
        #turn Ri once, U once
        return true
    
    if green[2][3] == "w" and red[2][1] == "o":
        #turn L once, Ui once
        return true
    if green[2][3] == "o" and red[2][1] == "w":
        #turn Bi once, U twice
        return true
                
    #if piece is in top layer
    for i in 3 and j in 3:
        if white[i][j] == "w":
            if orange[1][2] == "o":
                return true
            if green[1][2] == "o":
                #turn B twice, Di once, R twice
                return true
            if red[1][2] == "b":
                #turn Li twice, D twice, R twice
                return true
