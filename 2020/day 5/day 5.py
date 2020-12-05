# https://adventofcode.com/2020/day/5

def get_file(file_name):
    with open(file_name) as f:
        data = f.read().split("\n")[:-1]
    return(data)


def get_seat_id(data):
    return int("".join(["1" if i in "RB" else "0" for i in data]), 2)


def get_own_id(seat_list):
    return [seat_list[i] + 1 for i in range(len(seat_list) -1) if seat_list[i + 1] - seat_list[i] == 2][0]

 
def get_puzzle_answer(data):
    seat_list = sorted([get_seat_id(x) for x in data])
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
