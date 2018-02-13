class negativeError(Exception):
    def __str__(self):
        print "Invalid value, only positive numbers"
