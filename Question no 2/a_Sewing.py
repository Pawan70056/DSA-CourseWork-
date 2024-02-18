def calculate_min_moves(machines):
    total_dresses = sum(machines)
    n = len(machines)
    if total_dresses % n != 0:
        return -1
    average = total_dresses // n
    moves = 0
    balance = 0
    for dresses in machines:
        diff = dresses - average
        balance += diff
        moves += abs(balance)
    return moves

if __name__ == "__main__":
    input_line = input("Enter the number of dresses in each sewing machine separated by commas (e.g., 2, 1, 3, 0, 2):")
    machines = [int(x.strip()) for x in input_line.split(',')]
    result = calculate_min_moves(machines)
    print("Minimum number of moves required:", result)

