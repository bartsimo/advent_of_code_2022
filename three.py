
# read in data
def read_input(input_file):
    with open(input_file) as f:
        data_list = f.read().splitlines()

        return data_list



# check whether all strings have even length:
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
    for letter in first_half:
        if second_half.find(letter) != -1:
            return letter

def get_priority(s: str) -> int:
    if s.islower() == True:
        return ord(s) - 96
    else:
        return ord(s) - 38



def main():
    data_list = read_input("input3")
    answer = 0
    for gibberish in data_list:
        answer += get_priority(get_common_letter(gibberish))
    print(answer)




if __name__ == "__main__":
    main()

