package longestSubstring

// https://leetcode.com/problems/longest-substring-without-repeating-characters/
func lengthOfLongestSubstring(s string) int {
	var maxSubstringLen int

	seen := make([]*int, 128)
	var start int
	for i, r := range s {
		seenI := seen[r]
		if seenI == nil || *seenI < start {
			copyI := i
			seen[r] = &copyI
			continue
		}

		l := i - start
		if l > maxSubstringLen {
			maxSubstringLen = l
		}

		copyI := i
		seen[r] = &copyI
		start = *seenI + 1
	}

	l := len(s) - start
	if l > maxSubstringLen {
		maxSubstringLen = l
	}

	return maxSubstringLen
}
