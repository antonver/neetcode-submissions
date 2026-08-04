/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func reverseList(head *ListNode) *ListNode {
    var prev *ListNode
    next := head
    if head == nil{
        return head
    }
    for next.Next != nil{
        next = head.Next
        head.Next = prev
        prev = head
        head = next
    }
    head.Next = prev
    return head
}
