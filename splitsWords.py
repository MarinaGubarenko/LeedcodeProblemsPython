class Solution:
    """Class splits string by separator"""
    
    def splitWordsBySeparator(self, words, separator):
        """function returns an array of strings containing the new strings formed
        after the splits, excluding empty strings.

        Variable words contains a list of elements each of which is a string."""

        list_words = []
        for elem in words:
            for split_elem in elem.split(separator):
                if split_elem:
                    list_words.append(split_elem.strip())
        return list_words
