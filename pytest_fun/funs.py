# add a and b
def add(a, b):
    return a + b


# subtract b from a
def sub(a, b):
    return a - b


# calculate a squared
def square(a):
    return a*a


# write number to file
def write_int_to_file(a, file_path):
    file_path.write_text(str(a))


# sum up the values of a dict
def sum_dict(a):
    return(sum(a.values()))
