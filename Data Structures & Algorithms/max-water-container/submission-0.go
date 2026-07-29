func maxArea(heights []int) int {
max_area := 0.0
a := 0
b := len(heights) - 1
for a < b{
    max_area = math.Max((math.Min(float64(heights[a]), float64(heights[b])) * float64(b - a)), max_area)
    if heights[a] <= heights[b]{
        a++
    } else {
        b--
    }
    }
    return int(max_area)
}
