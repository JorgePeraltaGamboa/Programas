import time
global lifespan
lifespan=75
import lifespanError
import negativeError
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
