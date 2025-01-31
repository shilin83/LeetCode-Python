from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def arrayToList(arr: List[int]) -> Optional[ListNode]:
    head = None

    for item in reversed(arr):
        node = ListNode(item, head)
        head = node

    return head
