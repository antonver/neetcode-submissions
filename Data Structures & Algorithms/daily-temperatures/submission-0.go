func dailyTemperatures(temperatures []int) []int {
    result := make([]int, len(temperatures))
    stack := make([]int, 5)
    for i := range len(temperatures){
    for len(stack) > 0 && temperatures[i] > temperatures[stack[len(stack) - 1]]{
        result[stack[len(stack) - 1]] = i - stack[len(stack) - 1]
        stack = stack[:len(stack)-1]
    }
    stack = append(stack, i)
    }
    return result
}
