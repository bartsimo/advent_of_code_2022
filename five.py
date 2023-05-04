file_path = 'input5'


def read_input(txt_file):
    """Read the input file and return the table and orders as separate strings."""
    with open(txt_file, 'r') as f:
        lines = f.read()
        table, orders = lines.split('\n\n', 1)

        table = table.splitlines()

        orders = '\n'.join(line for line in orders.split('\n') if line.strip()).splitlines()

    return table, orders


def parse_stacks_from_table(table):
    """Parse the stacks from the table string and return them as a dictionary."""

    # Dynamically initialize data structure (dict) that stores stacks
    stacks = {i: [] for i, digit in enumerate(
        table[-1].replace(' ', ''), start=1) if digit != '9'}

    # Get indexes at which boxes could be stored:
    indexes = []
    for index, element in enumerate(table[-1]):
        if element != ' ':
            indexes.append(index)

    for i in range(len(table[:-1])):
        for j in indexes:
            if table[i][j].isalpha():
                stacks[i + 1].append(table[i][j])
            else:
                stacks[i + 1].append(' ')

    transposed = list(zip(*stacks.values()))
    for tup in range(len(transposed)):
        stacks[tup + 1] = list(transposed[tup])

    stacks = {k: [s for s in v if s.strip()] for k, v in stacks.items()}

    return stacks


def parse_orders(orders):
    """ Parse orders into list of lists where each inner list contains three ints: amount of boxes to be
     moved, source stack, target stack """
    clean_orders = []

    for order in orders:
        order = order.replace("move", "").replace("from ", "").replace("to ", "").strip().split(" ")
        order = [int(i) for i in order]
        clean_orders.append(order)

    return clean_orders

def move_boxes(stacks, orders):
    """Move boxes on stacks according to orders"""
    for i in orders:
        # move 8 from 3 to 2
        # They are moved one at a time, no slicing possible
        for j in range(i[0]):
            box_to_move = stacks[i[1]].pop(0)
            stacks[i[2]].insert(0, box_to_move)

    return stacks

def extract_solution(stacks):
    """Extract first box in every stack (is a list as values of the dict 'stacks') as a str."""
    first_elements = []
    for value in stacks.values():
        if value:
            first_elements.append(str(value[0]))

    solution = ''.join(first_elements)
    return solution




def main():
    table, orders = read_input(file_path)
    stacks = parse_stacks_from_table(table)
    clean_orders = parse_orders(orders)
    moved_stacks = move_boxes(stacks, clean_orders)
    solution = extract_solution(moved_stacks)
    print(solution)


if __name__ == "__main__":
    main()
    
