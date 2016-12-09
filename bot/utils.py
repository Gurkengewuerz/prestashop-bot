import random, string


def randomword(length):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(length))
