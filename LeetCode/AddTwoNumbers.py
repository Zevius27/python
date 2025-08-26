

# # Input: l1 = [2,4,3], l2 = [5,6,4]
# # Output: [7,0,8]
# # Explanation: 342 + 465 = 807.

# l1 = [2, 4, 3]
# l2 = [5, 6, 4]

# #  reverse ,
# #  append as a string ,
# #  change to int ,
# #  then add l1 and l2 into result ,
# #  reverse the result
# #  convert Into list
# #  return


# def AddTwoNumbers(z1, z2):
#     # reversed
#     z1.reverse()
#     z2.reverse()
#     # append as string
#     x = "".join(map(str, z1))
#     y = "".join(map(str, z2))
#     # change To int
#     x = int(x)  # Not changing to int
#     y = int(y)
#     #  then add z1 and z2 into z
#     z = x + y
#     # reverse the result
#     zr = int(str(z)[::-1])
#     # convert into string
#     zr = str(zr)
#     result = []
#     for i in zr:
#         # convert back to int
#         s = int(i)
#         result.append(s)
#     print(result)


# AddTwoNumbers(l1, l2)


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    """
    Add two numbers represented as linked lists in reverse order.

    Args:
        l1: ListNode - First number's linked list
        l2: ListNode - Second number's linked list

    Returns:
        ListNode - Sum as a linked list in reverse order

    Example:
        Input: l1 = [2,4,3], l2 = [5,6,4]
        Output: [7,0,8]
        Explanation: 342 + 465 = 807
    """
    dummy = ListNode(0)  # Dummy head to simplify logic
    current = dummy
    carry = 0

    # Process both lists while either has nodes or there's a carry
    while l1 or l2 or carry:
        # Get values from current nodes (0 if node is None)
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        # Calculate sum and new carry
        total = val1 + val2 + carry
        carry = total // 10
        digit = total % 10

        # Create new node with the digit
        current.next = ListNode(digit)
        current = current.next

        # Move to next nodes if they exist
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next  # Return head of result list


def create_linked_list(nums):
    """Helper function to create linked list from list of numbers"""
    if not nums:
        return None

    head = ListNode(nums[0])
    current = head
    for num in nums[1:]:
        current.next = ListNode(num)
        current = current.next
    return head


def linked_list_to_list(head):
    """Helper function to convert linked list back to list for display"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Test cases


    # Test case 1: 342 + 465 = 807
    # Represented as [2,4,3] + [5,6,4] = [7,0,8]
l1 = create_linked_list([2, 4, 3])
l2 = create_linked_list([5, 6, 4])
result = addTwoNumbers(l1, l2)
print(f"{linked_list_to_list(result)}")
