def get_file(file_name):
    with open(file_name) as f:
        data = f.read().split("\n\n")
    return(data)


def get_valid_documents(data):
    answer_1, answer_2 = 0, 0
    rec_fld = {
        "byr": {"min": 1920, "max": 2002},
        "iyr": {"min": 2010, "max": 2020},
        "eyr": {"min": 2020, "max": 2030},
        "hgt": {"cm":{"min": 150, "max":193}, "in":{"min":59, "max":76}},
        "hcl": "",
        "ecl": ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
        "pid": ""
        }
    for i in data:
        if all((x in i) for x in rec_fld):
            answer_1 += 1
            try:
                if (
                    rec_fld["byr"]["min"] <= int(i.split("byr:")[1][:4]) <= rec_fld["byr"]["max"] and #byr
                    rec_fld["iyr"]["min"] <= int(i.split("iyr:")[1][:4]) <= rec_fld["iyr"]["max"] and #iyr
                    rec_fld["eyr"]["min"] <= int(i.split("eyr:")[1][:4]) <= rec_fld["eyr"]["max"] and #eyr
                    (
                        rec_fld["hgt"][i.split("hgt:")[1].rsplit()[0][-2:]]["min"] <=
                        int(i.split("hgt:")[1].rsplit()[0][:-2]) <=
                        rec_fld["hgt"][i.split("hgt:")[1].rsplit()[0][-2:]]["max"]
                    ) and #hgt
                    i.split("hcl:")[1][0] == "#" and int(i.split("hcl:")[1][1:7], 16) is not ValueError and #hcl
                    i.split("ecl:")[1][:3] in rec_fld["ecl"] and #ecl
                    int(i.split("pid:")[1].rsplit()[0]) is not ValueError and len(i.split("pid:")[1].rsplit()[0]) == 9 #pid
                    ): 
                        answer_2 += 1
            except:
                continue
    return answer_1, answer_2


def main():
    data = get_file("input.txt")
    print(data)
    answer_1, answer_2 = get_valid_documents(data)
    print("answer 1:", answer_1)
    print("answer 2:", answer_2)


if __name__ == "__main__":
    main()