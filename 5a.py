import re
def ispno(num):
    if len(num) != 12:
        return False
    for i in range(len(num)):
        if i == 3 or i==7:
            if num[i]!='-':
                return False
        elif num[i].isdigit()==False:
            return False
    return True

def cpno(num):
    pp=re.compile(r'^\d{3}-\d{3}-\d{4}$')
    if pp.match(num):
        return True
    else:   
        return False

