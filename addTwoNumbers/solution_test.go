package addTwoNumbers

import "testing"

func Test_addTwoNumbers(t *testing.T) {
	tests := []struct {
		l1   *ListNode
		l2   *ListNode
		want *ListNode
	}{
		{
			l1:   listOf(2, 4, 3),
			l2:   listOf(5, 6, 4),
			want: listOf(7, 0, 8),
		},
		{
			l1:   listOf(0),
			l2:   listOf(0),
			want: listOf(0),
		},
		{
			l1:   listOf(9, 9, 9, 9, 9, 9, 9),
			l2:   listOf(9, 9, 9, 9),
			want: listOf(8, 9, 9, 9, 0, 0, 0, 1),
		},
	}
	for _, tt := range tests {
		sum := addTwoNumbers(tt.l1, tt.l2)
		if !equal(tt.want, sum) {
			t.Errorf("(%s + %s) = %s, want %s", tt.l1, tt.l2, sum, tt.want)
		}
	}
}

func listOf(v ...int) *ListNode {
	switch len(v) {
	case 0:
		return nil
	case 1:
		return &ListNode{Val: v[0]}
	}

	var (
		root    = &ListNode{Val: v[0]}
		current = root
	)
	for _, vv := range v[1:] {
		current.Next = &ListNode{Val: vv}
		current = current.Next
	}
	return root
}

func equal(expected *ListNode, actual *ListNode) bool {
	if expected == nil {
		return actual == nil
	}

	current := expected
	checked := actual
	for current != nil {
		if checked == nil || checked.Val != current.Val {
			return false
		}
		current = current.Next
		checked = checked.Next
	}

	return true
}
