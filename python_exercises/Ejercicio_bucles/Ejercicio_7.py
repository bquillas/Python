def my_sol():
    for i in range(1,11):
        for j in range(1,11):
            print("{}x{}={}".format(i,j,i*j))


def other_sol():
    for i in range(1,11):
        for j in range(1,11):
            print(i*j,end="\t")
        print("")


def run():
    my_sol()
    other_sol()


if __name__ == '__main__':
    run()