
# read in data
def read_input(input_file):
    with open(input_file) as f:
        # first, read() gives a string that is split into a list at line breaks by splitlines.
        data_list = f.read().splitlines()

        return data_list



# check whether all strings have even length (just to be sure):
"""
all_even = True
for i in data_list:
    if len(i) % 2 != 0:
        all_even = False

print(all_even)
"""
def get_common_letter(text: str) -> str:
    first_half = text[:(len(text)//2)]
    second_half = text[(len(text)//2):]
    # this works because we know from task three that there will be one common letter in both halves
    for letter in first_half:
        # the str built-in function returns -1 when no match is found
        if second_half.find(letter) != -1:
            # in this case, return this letter and leave loop
            return letter
    # if no match is found, return a string that is not a part of the dataset for sanity test
    # in order to hold contract of functions' signature
    return "$"


def get_priority(s: str) -> int:
    if s.islower() == True:
        # every str can be mapped to an ASCII value e.g. by the built in function ord()
        # subtracting 96 from lowercase letters ...
        return ord(s) - 96
    else:
        # ... and 38 from uppercase letters gives correct value according to specification in task 3
        return ord(s) - 38



def main():
    data_list = read_input("input3")
    answer = 0
    for gibberish in data_list:
        answer += get_priority(get_common_letter(gibberish))
    print(answer)




if __name__ == "__main__":
    main()

