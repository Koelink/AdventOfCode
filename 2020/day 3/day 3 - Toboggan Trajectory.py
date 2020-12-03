# https://adventofcode.com/2020/day/3

def get_file(file_name):
    with open(file_name) as f:
        data = f.readlines()  
    array = []
    for i in data:
        array.append([x for x in i if x != "\n"]) 
    return(array)


def down_slope(array, right, down):
    hit_trees = 0
    position = [0, 0]
    while True:
        if position[0] + down >= len(array):
            break
        else:
            position[0] = position[0] + down
        if position[1] + right >= len(array[0]):
            position[1] = position[1] + right - len(array[0])
        else:
            position[1] = position[1] + right
        if array[position[0]][position[1]] == "#":
            hit_trees += 1
    return hit_trees


def get_puzzle_answers(array):
    answer_1 = down_slope(array, 3, 1)
    answer_2_list = [[1, 1], [3,1], [5,1], [7,1], [1,2]]
    answer_2 = 1
    for i in answer_2_list:
        answer_2 *= down_slope(array, i[0], i[1])
    return answer_1, answer_2


def main():
    array = get_file("input.txt")
    answer_1, answer_2 = get_puzzle_answers(array)
    print("answer 1:", answer_1)
    print("answer 2:", answer_2)


if __name__ == "__main__":
    main()