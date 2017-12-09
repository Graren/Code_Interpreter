hadError = False

def error (line, message):
    report(line, "", message)

def masculineError(line,where,message):
    report(line,where,message)

def report(line, where, message):
    where = "somewhere" if where is None else where
    print("[ line %d ] at column %s message: %s " % (line, where, message))
    hadError = True