# read in data
def read_input(input_file):
    with open(input_file) as f:
        data_list = f.read().splitlines()
        data_list.pop()

    lol = []
    for i in data_list:
        splits = i.split(",")
        lol.append(splits)

    return lol


def is_useless(ls: list):
    min1, max1 = ls[0].split("-")
    min2, max2 = ls[1].split("-")
    ranges = (min1, max1, min2, max2)
    ranges_int = tuple(map(int, ranges))
    if ranges_int[0] <= ranges_int[2] and ranges_int[3] <= ranges_int[1] or ranges_int[2] <= ranges_int[0] and ranges_int[1] <= ranges_int[3]:
        return 1
    else:
        return 0

    

def main():
    result = 0
    lol = (read_input("input4"))
    for i in lol:
        result += is_useless(i)


    print(result)


if __name__ == "__main__":
    main()