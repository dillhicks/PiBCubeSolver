import numpy as np

top = yellow 
bottom = white
front = red
back = orange
left = blue
right = green




def translate9( string ):
    if( directions[i] == "R" ):
        return "B"     
    if( directions[i] == "R'"):
        return "B'"
    if( directions[i] == "L" ):
        return "F"
    if( directions[i] == "L'"):
        return "F'"
    if( directions[i] == "U" ):
        return "D"
    if( directions[i] == "U'" ):
        return "D'"
    if( directions[i] == "D" ):
        return "U"
    if( directions[i] == "D'" ):
        return "U'"
    if( directions[i] == "F" ):
        return "L"
    if( directions[i] == "F'" ):
        return "L'"
    if( directions[i] == "B" ):
        return "R"
    if( directions[i] == "B'" ):
        return "R'"

def translate10( string ):
    if( directions[i] == "R" ):
        return "R"     
    if( directions[i] == "R'"):
        return "R'"
    if( directions[i] == "L" ):
        return "L"
    if( directions[i] == "L'"):
        return "L'"
    if( directions[i] == "U" ):
        return "D"
    if( directions[i] == "U'" ):
        return "D'"
    if( directions[i] == "D" ):
        return "U"
    if( directions[i] == "D'" ):
        return "U'"
    if( directions[i] == "F" ):
        return "B"
    if( directions[i] == "F'" ):
        return "B'"
    if( directions[i] == "B" ):
        return "F"
    if( directions[i] == "B'" ):
        return "F'"

def translate11( string ):
    if( directions[i] == "R" ):
        return "F"     
    if( directions[i] == "R'"):
        return "F'"
    if( directions[i] == "L" ):
        return "B"
    if( directions[i] == "L'"):
        return "B'"
    if( directions[i] == "U" ):
        return "D"
    if( directions[i] == "U'" ):
        return "D'"
    if( directions[i] == "D" ):
        return "U"
    if( directions[i] == "D'" ):
        return "U'"
    if( directions[i] == "F" ):
        return "R"
    if( directions[i] == "F'" ):
        return "R'"
    if( directions[i] == "B" ):
        return "L"
    if( directions[i] == "B'" ):
        return "L'"

def translate12( string ):
    if( directions[i] == "R" ):
        return "L"     
    if( directions[i] == "R'"):
        return "L'"
    if( directions[i] == "L" ):
        return "R"
    if( directions[i] == "L'"):
        return "R'"
    if( directions[i] == "U" ):
        return "D"
    if( directions[i] == "U'" ):
        return "D'"
    if( directions[i] == "D" ):
        return "U"
    if( directions[i] == "D'" ):
        return "U'"
    if( directions[i] == "F" ):
        return "F"
    if( directions[i] == "F'" ):
        return "F"
    if( directions[i] == "B" ):
        return "B"
    if( directions[i] == "B'" ):
        return "B'"


def translate13( string ):
    if( directions[i] == "R" ):
        return "D"     
    if( directions[i] == "R'"):
        return "D'"
    if( directions[i] == "L" ):
        return "U"
    if( directions[i] == "L'"):
        return "U'"
    if( directions[i] == "U" ):
        return "F"
    if( directions[i] == "U'" ):
        return "F'"
    if( directions[i] == "D" ):
        return "B"
    if( directions[i] == "D'" ):
        return "B'"
    if( directions[i] == "F" ):
        return "L"
    if( directions[i] == "F'" ):
        return "L'"
    if( directions[i] == "B" ):
        return "R"
    if( directions[i] == "B'" ):
        return "R'"

def translate14( string ):
    if( directions[i] == "R" ):
        return "D"     
    if( directions[i] == "R'"):
        return "D'"
    if( directions[i] == "L" ):
        return "U"
    if( directions[i] == "L'"):
        return "U'"
    if( directions[i] == "U" ):
        return "L"
    if( directions[i] == "U'" ):
        return "L'"
    if( directions[i] == "D" ):
        return "R"
    if( directions[i] == "D'" ):
        return "R'"
    if( directions[i] == "F" ):
        return "B"
    if( directions[i] == "F'" ):
        return "B'"
    if( directions[i] == "B" ):
        return "F"
    if( directions[i] == "B'" ):
        return "F'"


def translate15( string ):
    if( directions[i] == "R" ):
        return "D"     
    if( directions[i] == "R'"):
        return "D'"
    if( directions[i] == "L" ):
        return "U"
    if( directions[i] == "L'"):
        return "U'"
    if( directions[i] == "U" ):
        return "B"
    if( directions[i] == "U'" ):
        return "B'"
    if( directions[i] == "D" ):
        return "F"
    if( directions[i] == "D'" ):
        return "F'"
    if( directions[i] == "F" ):
        return "R"
    if( directions[i] == "F'" ):
        return "R'"
    if( directions[i] == "B" ):
        return "L"
    if( directions[i] == "B'" ):
        return "L'"

def translate16( string ):
    if( directions[i] == "R" ):
        return "D"     
    if( directions[i] == "R'"):
        return "D'"
    if( directions[i] == "L" ):
        return "U"
    if( directions[i] == "L'"):
        return "U'"
    if( directions[i] == "U" ):
        return "R"
    if( directions[i] == "U'" ):
        return "R'"
    if( directions[i] == "D" ):
        return "L"
    if( directions[i] == "D'" ):
        return "L'"
    if( directions[i] == "F" ):
        return "F"
    if( directions[i] == "F'" ):
        return "F'"
    if( directions[i] == "B" ):
        return "B"
    if( directions[i] == "B'" ):
        return "B'"
