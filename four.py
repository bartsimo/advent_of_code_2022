# read in data
def read_input(input_file):
    # f is a file object
    with open(input_file) as f:
        # first, read() gives a string that is split into a list at line breaks by splitlines.
        data_list = f.read().splitlines()
        # last element useless, list is changed in-place
        data_list.pop()

    lol = []
    for i in data_list:
        # splits string at , returns result as list
        splits = i.split(",")
        lol.append(splits)

    return lol


def is_useless(ls: list):
    # splits string at -, returns tuple
    # works because of concrete form of str
    min1, max1 = ls[0].split("-")
    min2, max2 = ls[1].split("-")
    # create one tuple
    ranges = (min1, max1, min2, max2)
    # cast every tuple element to string
    ranges_int = tuple(map(int, ranges))
    # either one range is smaller than the other or the other is smaller than one or not
    if ranges_int[0] <= ranges_int[2] and ranges_int[3] <= ranges_int[1] or ranges_int[2] <= ranges_int[0] and ranges_int[1] <= ranges_int[3]:
        return 1
    else:
        return 0

    
# simple logic in one main function that calls helpers
def main():
    result = 0
    lol = (read_input("input4"))
    for i in lol:
        result += is_useless(i)


    print(result)


if __name__ == "__main__":
    main()