func twoSum(numbers []int, target int) []int {
 a := 0
 b := len(numbers) - 1
 for a < b {
    if numbers[a] + numbers[b] > target{
        b -= 1
    } else if numbers[a] + numbers[b] < target{
        a += 1
    } else{
        return []int{a + 1, b + 1}
    }
 }
 return []int{a, b}
}
