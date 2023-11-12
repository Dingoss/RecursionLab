class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head):
    if not head or not head.next:
        return head

    temp = head.val
    head.val = head.next.val
    head.next.val = temp

    head.next.next = swapPairs(head.next.next)

    return head
