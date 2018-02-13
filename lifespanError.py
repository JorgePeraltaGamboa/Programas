class lifespanError(Exception):
    def __str__(self):
        print "Age value exceeds normal lifespan"
