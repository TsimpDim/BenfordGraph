import re


def main():
    test_string = "awdwd0123dk34k2k4kk565n1jio34awd-21323wd,23.21"
    regex_pattern = r"[+-]?\d+(?:\.\d+)?"

    search = re.findall(regex_pattern, test_string)
    print(search)






if __name__ == "__main__":
    main()
