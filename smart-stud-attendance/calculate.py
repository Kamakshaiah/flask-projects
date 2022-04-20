def regNums(n):
    import random as rnd
    reg_nums = []

    for i in range(n):
        reg_nums.append(round(rnd.uniform(10000, 99999)))
    return reg_nums

def names(n):
    import string
    import random
    out = []
    for i in range(n):
        out.append(''.join(random.sample(string.ascii_lowercase, 5)))
    return out

def course(n):
    import string
    import random
    out = []
    for i in range(n):
        out.append(''.join(random.sample(string.ascii_lowercase, 3)))
    return out

def place(n):
    import string
    import random
    out = []
    for i in range(n):
        out.append(''.join(random.sample(string.ascii_lowercase, 3)))
    return out
