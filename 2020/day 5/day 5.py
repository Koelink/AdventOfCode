# https://adventofcode.com/2020/day/5

def get_file(file_name):
    with open(file_name) as f:
        data = f.read().split("\n")[:-1]
    return(data)


def get_seat_id(data):
    x = int("".join(["1" if i == "B" else "0" for i in data[:7]]),2)
    y = int("".join(["1" if i == "R" else "0" for i in data[7:]]),2)  
    return x * 8 + y


def get_own_id(seat_list):
    for i in range(max(seat_list)):
        if i not in seat_list:
            if i - 1 in seat_list and i + 1 in seat_list:
                return i


def get_puzzle_answer(data):
    seat_list = [get_seat_id(x) for x in data]
    answer_1 = max(seat_list)
    answer_2 = get_own_id(seat_list)
    return answer_1, answer_2


def main():
    data = get_file("input.txt")
    answer_1, answer_2 = get_puzzle_answer(data)
    print("answer 1:", answer_1)
    print("answer 2:", answer_2)


if __name__ == "__main__":
    main()
