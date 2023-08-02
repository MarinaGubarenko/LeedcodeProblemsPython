"""File contains the lunch of solving problems from leedcode"""


import splitsWords


if __name__ == '__main__':
    splitsWords = splitsWords.Solution()
    words = ["|||"]
    separator = "|"
    print(splitsWords.splitWordsBySeparator(words, separator))


