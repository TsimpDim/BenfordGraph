import re
import matplotlib

def main():

    frequencies = [0] * 10

    test_string = "awdwd0123dk34k2k4kk565n1jio34awd-21323wd,23.21"
    regex_pattern = r"[+-]?\d+(?:\.\d+)?"

    search = re.findall(regex_pattern, test_string)
    for i, numb in enumerate(search):
        #Strip leading zeroes and the signs
        search[i] = numb.strip("0")
        search[i] = search[i].strip("-")
        search[i] = search[i].strip("+")

        #Calculate the frequencies
        frequencies[int(search[i][0])] += 1

    print(search)
    print(frequencies)

    







if __name__ == "__main__":
    main()
