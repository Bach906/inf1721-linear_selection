import csv
from random import randint


def gen_file(size):
    file_name = "n" + str(size) + ".txt"
    f = open(file_name, "w")
    
    for count in range(size):

        n = randint(0, 100000)
        f.write(str(n))
        if count != size - 1:
            f.write("\n")

    f.close()
    return

def main():

    for i in range(1000, 10001, 1000):
        gen_file(i)

    return

main()