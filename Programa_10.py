import time
global lifespan
lifespan=75
#Class expception lifespan
class lifespanError(Exception):
    def __str__(self):
        print "Age value exceeds normal lifespan"
#Class expception negatives
class negativeError(Exception):
    def __str__(self):
        print "Invalid value, only positive numbers"

def age_diference(birth_year):
    try:
        if(birth_year<0):
            raise negativeError()
        elif (int(time.strftime("%Y"))-birth_year > lifespan):
            raise lifespanError()
    except TypeError:
        print "Incompatible types"
    except lifespanError:
        print "Age value exceeds normal lifespan"
    except negativeError:
        print "Invalid value, only positive numbers"
    else:
        print int(time.strftime("%Y"))-birth_year

age_diference(1996)
age_diference(1800)
age_diference("New Hope")
age_diference(-1996)
