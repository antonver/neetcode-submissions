func maxProfit(prices []int) int {
dif := 0
min_ := prices[0]
for _, i := range prices[1:]{
	if i - min_ > dif{
		dif = i - min_
	}
	if min_ > i{
		min_ = i
	}

}
return dif
}
