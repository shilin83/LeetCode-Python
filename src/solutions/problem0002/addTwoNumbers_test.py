import pytest

from typing import List
from .addTwoNumbers import Solution
from ...structures.linkedList import arrayToList

testdata = [
    ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
    ([0], [0], [0]),
    ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
]


@pytest.mark.parametrize("nums1, nums2, expected", testdata)
def test_addTwoNumbers(nums1: List[int], nums2: List[int], expected: List[int]) -> None:
    solution = Solution()

    expected = arrayToList(expected)
    actual = solution.addTwoNumbers(arrayToList(nums1), arrayToList(nums2))

    while expected is not None and actual is not None:
        assert expected.val == actual.val

        expected = expected.next
        actual = actual.next
