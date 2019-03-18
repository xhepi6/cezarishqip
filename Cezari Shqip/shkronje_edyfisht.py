

def shkronje_edyfisht(shkronja,fjalia):
    shkronja = shkronja.upper()
    fjalia = list(fjalia.upper())
    nr = fjalia.index(shkronja)
    if shkronja == 'D':
        if fjalia[nr+1] == 'H':
            return True
    elif shkronja == 'G':
        if fjalia[nr+1] == 'J':
            return True
    elif shkronja == 'L':
        if fjalia[nr+1] == 'L':
            return True
    elif shkronja == 'N':
        if fjalia[nr+1] == 'J':
            return True
    elif shkronja == 'R':
        if fjalia[nr+1] == 'R':
            return True
    elif shkronja == 'S':
        if fjalia[nr+1] == 'H':
            return True
    elif shkronja == 'T':
        if fjalia[nr+1] == 'H':
            return True
    elif shkronja == 'X':
        if fjalia[nr+1] == 'H':
            return True
    elif shkronja == 'Z':
        if fjalia[nr+1] == 'H':
            return True
    else:
        return False
    
    
        
