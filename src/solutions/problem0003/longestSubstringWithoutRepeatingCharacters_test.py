import pytest

from longestSubstringWithoutRepeatingCharacters import Solution

testdata = [
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3),
]


@pytest.mark.parametrize("s, expected", testdata)
def test_lengthOfLongestSubstring(s: str, expected: int) -> None:
    solution = Solution()

    assert solution.lengthOfLongestSubstring(s) == expected
