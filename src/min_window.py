"""
from Leet Code, slightly modifed problem statement to a different problem version

Given a string S and a string T, find the minimum window in S which will contain all the unique characters in T in
complexity O(n).

Example:
Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"

Note:
If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
"""


def satisfied(contains):
    for i in contains:
        if contains[i] == 0:
            return False
    return True


def min_window(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """

    # edge case, target is empty string
    if t == '':
        return ''

    match = None
    contains = {i: 0 for i in t}
    wanted = set()
    for i in t:
        wanted.add(i)
    start = None
    i = 0

    while i < len(s):
        if s[i] in wanted:
            if start is None:
                start = i
            contains[s[i]] += 1
            while satisfied(contains):
                if start == len(s) - 1:
                    break
                cur_match = s[start:i + 1]
                if match is None:
                    match = cur_match
                elif len(cur_match) < len(match):
                    match = cur_match
                contains[s[start]] -= 1
                start += 1
                while start < len(s):
                    if s[start] not in wanted:
                        start += 1
                    else:
                        break
                if start == len(s) - 1:
                    i = len(s) - 1  # so that outer most while loop terminates
                # contains[s[start]] += 1
        i += 1

    # check the last group
    if satisfied(contains):
        cur_match = s[start:i + 1]
        if match is None:
            match = cur_match
        elif len(cur_match) < len(match):
            match = cur_match

    # edge case of no match
    if match is None:
        return ''
    else:
        return match
