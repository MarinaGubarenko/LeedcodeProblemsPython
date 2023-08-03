"""File contains the lunch of solving problems from leedcode"""


import splitsWords
import arrayIsGood


if __name__ == '__main__':
    # solution task 2788 split words by separator
    splitsWords = splitsWords.Solution()
    words = ["|||"]
    separator = "|"
    print(splitsWords.splitWordsBySeparator(words, separator))

    # solution task 2784. Check if Array is Good
    nums = [3, 4, 4, 1, 2, 1]
    arrayIsGood = arrayIsGood.Solution()
    print(arrayIsGood.isGood(nums))




