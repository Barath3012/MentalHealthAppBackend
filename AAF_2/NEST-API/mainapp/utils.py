from datetime import date


def getDate(s):
    doearr=s.split("-")
    if len(doearr)<3:
        return False    
    doe=date(int(doearr[0]),int(doearr[1]),int(doearr[2]))
    return doe