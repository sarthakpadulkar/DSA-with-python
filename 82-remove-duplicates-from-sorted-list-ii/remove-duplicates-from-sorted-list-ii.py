class Solution:
    def deleteDuplicates(self, head):
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        current = head

        while current:
            if current.next and current.val == current.next.val:
                duplicate = current.val

                while current and current.val == duplicate:
                    current = current.next

                prev.next = current

            else:
                prev = current
                current = current.next

        return dummy.next