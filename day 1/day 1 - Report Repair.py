def get_file(file_name):
    with open(file_name) as f:
        data = [int(x) for x in f.readlines()]
    return(data)


def get_puzzle_answer(data):
    for y in data:
        for x in data:
            if x + y == 2020:
                answer_1 = x * y
            for z in data:
                if x + y + z == 2020:
                    answer_2 = x * y * z
    return answer_1, answer_2


def main():
    data = get_file("input.txt")
    answer_1, answer_2 = get_puzzle_answer(data)
    print("answer 1:", answer_1)
    print("answer 2:", answer_2)


if __name__ == "__main__":
    main()
