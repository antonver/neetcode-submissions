import "slices"

func carFleet(target int, position []int, speed []int) int {
	fleet := 0
	min_time := 0.0
	postions := make([][2]int, len(position))
	for i := range len(postions){
		postions[i][0] = position[i]
		postions[i][1] = speed[i]
	}
	slices.SortFunc(postions, func(a [2]int, b [2]int) int{
		return b[0] - a[0]
	})
	for _, car := range postions{
		t := (float64(target) - float64(car[0])) / float64(car[1])
		if t > min_time {
			fleet += 1
			min_time = t
		}
	}
	return fleet
}
