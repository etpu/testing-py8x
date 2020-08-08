import string

def isvalid(password):
    has_no = set(password).isdisjoint
    print(has_no)
    print(has_no(string.digits), has_no(string.ascii_lowercase), has_no(string.ascii_uppercase))

    return not (len(password) < 10
                or has_no(string.digits)
                or has_no(string.ascii_lowercase)
                or has_no(string.ascii_uppercase))


isvalid('bAse730onE4')