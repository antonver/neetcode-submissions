func search(nums []int, target int) int {
pivot := 0
a := 0
b := len(nums) - 1
for a <= b{
	pivot = a + (b - a) / 2
	if nums[pivot] > target{
		b = pivot - 1
	} else if nums[pivot] < target{
		a = pivot + 1
	} else {
		return pivot
	}
}
return -1
}
