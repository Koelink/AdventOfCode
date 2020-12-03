def get_file(file_name):
    with open(file_name) as f:
        data = f.readlines()
    return(data)


def get_valid_passwords(data):
    x, y = 0, 0
    for i in data:
        first_nr = int(i.split("-")[0])        
        second_nr = int(i.split("-")[1].split(" ")[0])
        character = i.split(" ")[1].split(":")[0]
        password = i.split(" ")[2]
        if first_nr <= password.count(character) <= second_nr:
            x += 1
        if (password[first_nr -1] == character) != (password[second_nr -1] == character):
            y += 1
    return x, y


def main():
    data = get_file("input.txt")
    answer_1, answer_2 = get_valid_passwords(data)
    print("answer 1:", answer_1)
    print("answer 2:", answer_2)


if __name__ == "__main__":
    main()