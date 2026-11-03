class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head
        curr = head
        length = 1
        while curr.next:
            curr = curr.next
            length += 1
        k %= length
        if k == 0:
            return head
        curr.next = head
        new_tail = head
        for i in range(length - k - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        return new_head