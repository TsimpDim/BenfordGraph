import sys
from re import findall
import matplotlib.pyplot as plt
import numpy as np


def main():

    frequencies = [0] * 10
    leading_numbers = []

    text = open(sys.argv[1], "r").read()
    regex_pattern = r"[+-]?\d+(?:\.\d+)?"

    search = findall(regex_pattern, text)
    for i, numb in enumerate(search):

        # Strip leading zeroes and the signs
        if "0." in search[i] or "0," in search[i]:
            continue

        search[i] = numb.strip("0")
        search[i] = search[i].strip("-")
        search[i] = search[i].strip("+")

        # Seperate leading numbers
        if search[i]:
            leading = int(search[i][0])
            if leading not in leading_numbers:
                leading_numbers.append(leading)

        # Calculate the frequencies
        frequencies[leading] += 1

    leading_numbers.sort()

    # Hold only the non-zero elements
    frequencies_subset = frequencies[leading_numbers[0]: leading_numbers[-1] + 1]

    # Calculate theoretical distribution of digits

    distribution = []
    sum_of_freq = sum(frequencies_subset)
    for num in leading_numbers:
        distribution.append(benford_distribution(num) * sum_of_freq)

    # print(search)
    # print(leading_numbers)
    # print(frequencies)
    # print(frequencies_subset)

    plt.plot(leading_numbers, distribution, label="Benford Distribution")
    plt.plot(leading_numbers, frequencies_subset, label="Actual Distribution", marker=".")
    plt.title("Benford Curve")
    plt.ylabel("Frequencies of Leading")
    plt.xlabel("Leading Digits")
    plt.legend()
    plt.show()


def benford_distribution(d):
    '''Returns the distribution percentage of the given (d)igit'''
    return np.log10(1 + 1/d)


if __name__ == "__main__":
    main()
