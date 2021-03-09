package addTwoNumbers

import (
	"strconv"
	"strings"
)

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
type ListNode struct {
	Val  int
	Next *ListNode
}

func (l *ListNode) String() string {
	if l == nil {
		return "[]"
	}

	var buf strings.Builder
	buf.WriteString("[")

	var (
		current = l
		first   = true
	)
	for current != nil {
		if !first {
			buf.WriteString(", ")
		}

		buf.WriteString(strconv.Itoa(current.Val))
		first = false

		current = current.Next
	}
	buf.WriteString("]")

	return buf.String()
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	var (
		carry, num   int
		root, result *ListNode
	)
	for l1 != nil && l2 != nil {
		num, carry = adjust(l1.Val + l2.Val + carry)

		if result == nil {
			root = &ListNode{}
			result = root
		} else {
			result.Next = &ListNode{}
			result = result.Next
		}

		result.Val = num

		l1 = l1.Next
		l2 = l2.Next
	}

	for l1 != nil {
		num, carry = adjust(l1.Val + carry)

		result.Next = &ListNode{}
		result = result.Next
		result.Val = num

		l1 = l1.Next
	}

	for l2 != nil {
		num, carry = adjust(l2.Val + carry)

		result.Next = &ListNode{}
		result = result.Next
		result.Val = num

		l2 = l2.Next
	}

	if carry > 0 {
		result.Next = &ListNode{}
		result = result.Next
		result.Val = carry
	}

	return root
}

func adjust(sum int) (int, int) {
	if sum > 9 {
		return sum - 10, 1
	}
	return sum, 0
}
