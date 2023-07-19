def longest_palindromic_substring(A):
    if not A:
        return ""

    longest = ""
    max_length = 0

    for i in range(len(A)):
        left = right = i
        while left >= 0 and right < len(A) and A[left] == A[right]:
            if right - left + 1 > max_length:
                max_length = right - left + 1
                longest = A[left:right+1]
            left -= 1
            right += 1
        left = i
        right = i + 1
        while left >= 0 and right < len(A) and A[left] == A[right]:
            if right - left + 1 > max_length:
                max_length = right - left + 1
                longest = A[left:right+1]
            left -= 1
            right += 1

    return longest
A = input()
print(longest_palindromic_substring(A))

"""
Input 1:
A = "aaaabaaa"

Input 2:
A = "abba


Output 1:
"aaabaaa"

Output 2:
"abba"
"""

