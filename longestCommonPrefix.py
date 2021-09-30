from typing import List


def longestCommonPrefix(str :List[str]):
    lcp=''
    for row in zip(*str):
        if all(i == row[0] for i in row):
            lcp += row[0]
        else:
            return lcp
    return lcp

