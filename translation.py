def translate1(string):
    return string
def translate2(string):
    if string == "r":
        return "f"
    if string == "r'":
        return "f'"
    if string == "l":
        return "b"
    if string == "l'":
        return "b'"
    if string == "d":
        return "d"
    if string == "d'":
        return "d'"
    if string == "u":
        return "u"
    if string == "u'":
        return "u'"
    if string == "f":
        return "l"
    if string == "f'":
        return "l'"
    if string == "b":
        return "r"
    if string == "b'":
        return "r'"

def translate3(string):
    if string == "r":
        return "l"
    if string == "r'":
        return "l'"
    if string == "l":
        return "r"
    if string == "l'":
        return "r'"
    if string == "d":
        return "d"
    if string == "d'":
        return "d'"
    if string == "u":
        return "u"
    if string == "u'":
        return "u'"
    if string == "b":
        return "f"
    if string == "b'":
        return "f'"
    if string == "f":
        return "b"
    if string == "f'":
        return "b'"

def translate4(string):
    if string == "r":
        return "b"
    if string == "r'":
        return "b'"
    if string == "l":
        return "f"
    if string == "l'":
        return "f'"
    if string == "d":
        return "d"
    if string == "d'":
        return "d'"
    if string == "u":
        return "u"
    if string == "u'":
        return "u'"
    if string == "b":
        return "l"
    if string == "b'":
        return "l'"
    if string == "f":
        return "r"
    if string == "f'":
        return "r'"
def translate5(string):
    if string == "r":
        return "u"
    if string == "r'":
        return "u'"
    if string == "l":
        return "d"
    if string == "l'":
        return "d'"
    if string == "d":
        return "b"
    if string == "d'":
        return "b'"
    if string == "u":
        return "f"
    if string == "u'":
        return "f'"
    if string == "b":
        return "l"
    if string == "b'":
        return "l'"
    if string == "f":
        return "r"
    if string == "f'":
        return "r'"
def translate6(string):
    if string == "r":
        return "u"
    if string == "r'":
        return "u'"
    if string == "l":
        return "d"
    if string == "l'":
        return "d'"
    if string == "d":
        return "r"
    if string == "d'":
        return "r'"
    if string == "u":
        return "l"
    if string == "u'":
        return "l'"
    if string == "b":
        return "b"
    if string == "b'":
        return "b'"
    if string == "f":
        return "f"
    if string == "f":
        return "f'"
def translate7(string):
    if string == "r":
        return "u"
    if string == "r'":
        return "u'"
    if string == "l":
        return "d"
    if string == "l'":
        return "d'"
    if string == "d":
        return "f"
    if string == "d'":
        return "f'"
    if string == "u":
        return "b"
    if string == "u'":
        return "b'"
    if string == "b":
        return "r"
    if string == "b'":
        return "r'"
    if string == "f":
        return "l"
    if string == "f":
        return "l'"
def translate8(string):
    if string == "r":
        return "u"
    if string == "r'":
        return "u'"
    if string == "l":
        return "d"
    if string == "l'":
        return "d'"
    if string == "d":
        return "l"
    if string == "d'":
        return "l'"
    if string == "u":
        return "r"
    if string == "u'":
        return "r'"
    if string == "b":
        return "f"
    if string == "b'":
        return "f'"
    if string == "f":
        return "b"
    if string == "f":
        return "b'" 
    
def translate17( move ):
	if move == "U":
		return "F"
	if move == "D":
		return "B"
	if move == "F":
		return "D"
	if move == "B":
		return "U'"
	if move == "L":
		return "L"
	if move == "R":
		return "R"
	#counter
	if move == "U'":
		return "F'"
	if move == "D'":
		return "B'"
	if move == "F'":
		return "D'"
	if move == "B'":
		return "U'"
	if move == "L'":
		return "L'"
	if move == "R'":
		return "L'"
# [0] = top, [1] = front, [2] = left, [3] = right, [4] = back, [5] = bottom
#orient18 = np.array([r, g, w, y, b, o])
def translate18( move ):
	if move == "U":
		return "F"
	if move == "D":
		return "B"
	if move == "F":
		return "R"
	if move == "B":
		return "L"
	if move == "L":
		return "B"
	if move == "R":
		return "U"
	#counter
	if move == "U'":
		return "F'"
	if move == "D'":
		return "B'"
	if move == "F'":
		return "R'"
	if move == "B'":
		return "L'"
	if move == "L'":
		return "B'"
	if move == "R'":
		return "U'"
# [0] = top, [1] = front, [2] = left, [3] = right, [4] = back, [5] = bottom
#orient19 = np.array([r, y, g, b, w, o])
def translate19( move ):
	if move == "U":
		return "F"
	if move == "D":
		return "B"
	if move == "F":
		return "U"
	if move == "B":
		return "D"
	if move == "L":
		return "R"
	if move == "R":
		return "L"
	#counter
	if move == "U'":
		return "F'"
	if move == "D'":
		return "B'"
	if move == "F'":
		return "U'"
	if move == "B'":
		return "D'"
	if move == "L'":
		return "R'"
	if move == "R'":
		return "L'"
# [0] = top, [1] = front, [2] = left, [3] = right, [4] = back, [5] = bottom
#orient20 = np.array([r, b, y, w, g, o])
def translate20( move ):
	if move == "U":
		return "F"
	if move == "D":
		return "B"
	if move == "F":
		return "L"
	if move == "B":
		return "R"
	if move == "L":
		return "U"
	if move == "R":
		return "D"
	#counter
	if move == "U'":
		return "F'"
	if move == "D'":
		return "B'"
	if move == "F'":
		return "L'"
	if move == "B'":
		return "R'"
	if move == "L'":
		return "U'"
	if move == "R'":
		return "D'"
# [0] = top, [1] = front, [2] = left, [3] = right, [4] = back, [5] = bottom
#orient21 = np.array([o, b, w, y, g, r])
def translate21( move ):
	if move == "U":
		return "F"
	if move == "D":
		return "B"
	if move == "F":
		return "L"
	if move == "B":
		return "R"
	if move == "L":
		return "U"
	if move == "R":
		return "D"
	#counter
	if move == "U'":
		return "F'"
	if move == "D'":
		return "B'"
	if move == "F'":
		return "L'"
	if move == "B'":
		return "R'"
	if move == "L'":
		return "U'"
	if move == "R'":
		return "D'"
# [0] = top, [1] = front, [2] = left, [3] = right, [4] = back, [5] = bottom
#orient22 = np.array([o, y, b, g, w, r])
def translate22( move ):
	if move == "U":
		return "B"
	if move == "D":
		return "F"
	if move == "F":
		return "U"
	if move == "B":
		return "D"
	if move == "L":
		return "L"
	if move == "R":
		return "R"
	#counter
	if move == "U'":
		return "B'"
	if move == "D'":
		return "F'"
	if move == "F'":
		return "U'"
	if move == "B'":
		return "D'"
	if move == "L'":
		return "L'"
	if move == "R'":
		return "R'"

# [0] = top, [1] = front, [2] = left, [3] = right, [4] = back, [5] = bottom
#orient23 = np.array([o, g, y, w, b, r])
def translate23( move ):
	if move == "U":
		return "B"
	if move == "D":
		return "F"
	if move == "F":
		return "R"
	if move == "B":
		return "L"
	if move == "L":
		return "U"
	if move == "R":
		return "D"
	#counter
	if move == "U'":
		return "B'"
	if move == "D'":
		return "F'"
	if move == "F'":
		return "R'"
	if move == "B'":
		return "L'"
	if move == "L'":
		return "U'"
	if move == "R'":
		return "D'"

# [0] = top, [1] = front, [2] = left, [3] = right, [4] = back, [5] = bottom
#orient24 = np.array([o, w, g, b, y, r])
def translate24( move ):
	if move == "U":
		return "B"
	if move == "D":
		return "F"
	if move == "F":
		return "D"
	if move == "B":
		return "U"
	if move == "L":
		return "R"
	if move == "R":
		return "L"
	#counter
	if move == "U'":
		return "B'"
	if move == "D'":
		return "F'"
	if move == "F'":
		return "D'"
	if move == "B'":
		return "U'"
	if move == "L'":
		return "L'"
	if move == "R'":
		return "R'"

