import sys
from re import findall
import matplotlib.pyplot as plt

def main():

    frequencies = [0] * 10
    leading_numbers = []

    text = open(sys.argv[1], "r").read()
    regex_pattern = r"[+-]?\d+(?:\.\d+)?"

    search = findall(regex_pattern, text)
    for i, numb in enumerate(search):
        #Strip leading zeroes and the signs
        search[i] = numb.strip("0")
        search[i] = search[i].strip("-")
        search[i] = search[i].strip("+")

        #Seperate leading numbers
        leading = int(search[i][0])
        if leading not in leading_numbers:
            leading_numbers.append(leading)

        #Calculate the frequencies
        frequencies[leading] += 1

    leading_numbers.sort()

    #Hold only the non-zero elements
    frequencies_subset = frequencies[leading_numbers[0] : leading_numbers[-1] + 1]


    #print(search)
    #print(leading_numbers)
    #print(frequencies)
    #print(frequencies_subset)

    plt.plot(leading_numbers, frequencies_subset)
    plt.show()







if __name__ == "__main__":
    main()
