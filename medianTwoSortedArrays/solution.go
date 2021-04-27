package medianTwoSortedArrays

// https://leetcode.com/problems/median-of-two-sorted-arrays/
func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	if len(nums1) == 0 && len(nums2) == 0 {
		return 0.0
	}

	nums := mergeArrays(nums1, nums2)
	size := len(nums)

	var median float64
	if size%2 == 0 {
		median = float64((nums[size/2-1] + nums[size/2])) / 2.0
	} else {
		median = float64(nums[size/2])
	}

	return median
}

func mergeArrays(arr1, arr2 []int) []int {
	arr := make([]int, 0, len(arr1)+len(arr2))

	i, j := 0, 0
	for i < len(arr1) && j < len(arr2) {
		if arr1[i] < arr2[j] {
			arr = append(arr, arr1[i])
			i++
		} else {
			arr = append(arr, arr2[j])
			j++
		}
	}

	for ; i < len(arr1); i++ {
		arr = append(arr, arr1[i])
	}

	for ; j < len(arr2); j++ {
		arr = append(arr, arr2[j])
	}

	return arr
}
