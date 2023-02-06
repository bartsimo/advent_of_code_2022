
# read in data
def read_input(input_file):
    with open(input_file) as f:
        data_list = f.read().splitlines()

        # print(len(data_list) % 3)

        return data_list

def get_groups_of_three(data_list: list) -> list:
    data_list_threes = []
    while len(data_list) > 0:
    # Ab hier!
        counter = 0
        group = []
        while counter < 3:
            group.append(data_list.pop())
            counter += 1
        data_list_threes.append(group)


    return data_list_threes
        


def get_common_letter(group: list) -> str:
    group_of_sets = []

    for member in group:
        member_as_set = set(member)
        group_of_sets.append(member_as_set)

    return group_of_sets[0].intersection(group_of_sets[1], group_of_sets[2]).pop()


def get_priority(s: str) -> int:
    if s.islower() == True:
        return ord(s) - 96
    else:
        return ord(s) - 38



def main():
    data_list = read_input("input3")
    data_list_threes = get_groups_of_three(data_list)
    answer = 0
    for group in data_list_threes:
        answer += get_priority(get_common_letter(group))
    print(answer)




if __name__ == "__main__":
    main()

