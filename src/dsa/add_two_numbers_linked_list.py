from platform import node


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1,l2):

        temp_1 = l1
        temp_2 = l2
        temp_3 = ListNode(0)
        result = temp_3
        carry = 0
        _add = ""
        while temp_1 != None and temp_2 != None:
            if carry > 0:
                _add = str(temp_1.val+ temp_2.val+carry)
                carry = 0
            else:
                _add = str(temp_2.val+ temp_1.val)
            if len(_add) >= 2:
                carry = int(_add[0])
                node_add = ListNode(_add[1])
                temp_3.next = node_add
                temp_3 = temp_3.next
            else:
                node_add = ListNode(_add[0])
                temp_3.next = node_add
                temp_3 = temp_3.next
            temp_1 = temp_1.next
            temp_2 = temp_2.next

        while(temp_2 != None):
            if carry > 0:
                _add = str(temp_2.val + carry)
                carry = 0
            else:
                _add = str(temp_2.val)
            if len(_add) >= 2:
                carry = int(_add[0])
                node_add = ListNode(_add[1])
                temp_3.next = node_add
                temp_3 = temp_3.next
            else:
                node_add = ListNode(_add[0])
                temp_3.next = node_add
                temp_3 = temp_3.next
            temp_2 = temp_2.next

        while (temp_1 != None):
            if carry > 0:
                _add = str(temp_1.val + carry)
                carry = 0
            else:
                _add = str(temp_1.val)
            if len(_add) >= 2:
                carry = int(_add[0])
                node_add = ListNode(_add[1])
                temp_3.next = node_add
                temp_3 = temp_3.next
            else:
                node_add = ListNode(_add[0])
                temp_3.next = node_add
                temp_3 = temp_3.next
            temp_1 = temp_1.next
        if carry >0:
            node_add = ListNode(_add[0])
            temp_3.next = node_add
            temp_3 = temp_3.next
        return result.next

l1_head = ListNode(2)
l1_head.next = ListNode(4)
l1_head.next.next = ListNode(3)

l2_head = ListNode(5)
l2_head.next = ListNode(6)
l2_head.next.next = ListNode(4)

obj = Solution()
print(obj.addTwoNumbers(l1_head,l2_head))





