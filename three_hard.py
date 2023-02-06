
# read in data
def read_input(input_file):
    # return file object
    with open(input_file) as f:
        # first, read() gives a string that is split into a list at line breaks by splitlines.
        data_list = f.read().splitlines()

        # make sure that dataset is divisible by three
        # print(len(data_list) % 3)

        return data_list

def get_groups_of_three(data_list: list) -> list:
    # create list of list of three entries
    data_list_threes = []
    # go through dataset
    while len(data_list) > 0:
        counter = 0
        # fill a group with three entries and save this group as a list
        group = []
        while counter < 3:
            group.append(data_list.pop())
            counter += 1
        data_list_threes.append(group)


    return data_list_threes
        


def get_common_letter(group: list) -> str:
    group_of_sets = []

    # save every string as a set (no duplicates but valid since we are ultimately interested in a str of length 1)
    for member in group:
        member_as_set = set(member)
        group_of_sets.append(member_as_set)

    # find intersection of three sets and return the intersection
    return group_of_sets[0].intersection(group_of_sets[1], group_of_sets[2]).pop()

# see three.py
def get_priority(s: str) -> int:
    if s.islower() == True:
        return ord(s) - 96
    else:
        return ord(s) - 38


# run programm with one main function that calls helper functions
def main():
    data_list = read_input("input3")
    data_list_threes = get_groups_of_three(data_list)
    answer = 0
    for group in data_list_threes:
        answer += get_priority(get_common_letter(group))
    print(answer)




if __name__ == "__main__":
    main()

