
def get_input(file) -> list:
    # f is a file object
    with open(file) as f:
        # first, read() gives a string that is split into a list at line breaks by splitlines.
        calories = f.read().splitlines()

    # removes last empty list element
    calories.pop()

    return calories

def find_max_calories(ls: list) -> int:
    calories_per_elf = []
    # make current_calories accessible in the loop
    current_calories = 0
    for food in ls:
        if food != "":
            current_calories += int(food)
        elif food == "":
            calories_per_elf.append(current_calories)
            # start with new elf
            current_calories = 0
    #necessary because I popped last empty element in file I/O, treats first if clause in loop for last elf
    calories_per_elf.append(current_calories)

    return max(calories_per_elf)

# run core logic from one main function
def main():
    calories = get_input("input1")
    print(find_max_calories(calories))


if __name__ == "__main__":
    main()