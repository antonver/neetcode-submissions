

func largestRectangleArea(heights []int) int {
stack := []int{}
max_area := 0
left := -1
height := 0
heights = append(heights, 0)
for i,h := range heights{
for len(stack) > 0 && heights[stack[len(stack) - 1]] > h {
height = heights[stack[len(stack) - 1]]
stack = stack[:len(stack)-1]
if len(stack) > 0{
left = stack[len(stack)-1]
} else{
left = -1
}
width := i - left - 1
max_area = max(max_area, width * height)

} 
stack = append(stack, i)
}
return max_area
}