package twoSum

func twoSum(nums []int, target int) []int {
	var firstI, secondI int
mainLoop:
	for i := 0; i < len(nums); i++ {
		firstI = i
		secondPart := target - nums[firstI]
		for secondI = i + 1; secondI < len(nums); secondI++ {
			if secondPart == nums[secondI] {
				break mainLoop
			}
		}
	}

	if firstI >= len(nums) || secondI >= len(nums) {
		return []int{}
	}

	return []int{firstI, secondI}
}

func twoSumHash(nums []int, target int) []int {
	numIndices := make(map[int]int, len(nums))
	for i, num := range nums {
		numIndices[num] = i
	}

	for firstI := 0; firstI < len(nums); firstI++ {
		secondPart := target - nums[firstI]
		secondI, ok := numIndices[secondPart]
		if ok && secondI != firstI {
			return []int{firstI, secondI}
		}
	}

	return []int{}
}

func twoSumHashOnePass(nums []int, target int) []int {
	numIndices := make(map[int]int, len(nums))
	for firstI, num := range nums {
		secondPart := target - num
		secondI, ok := numIndices[secondPart]
		if ok && secondI != firstI {
			return []int{firstI, secondI}
		}

		numIndices[num] = firstI
	}

	return []int{}
}
