import "slices"

func threeSum(nums []int) [][]int {
slices.Sort(nums)
res := [][]int{}
for i:= range len(nums) - 1{
    a := i + 1
    b := len(nums) - 1
    target := 0
    for a < b{
        if  nums[i] + nums[b] + nums[a] < target{
            a++
        }else if b == i || nums[i] + nums[b] + nums[a] > target{
            b--
        } else{
        sl := []int{nums[i], nums[a], nums[b]}
        j := 0
        for _, k := range res{
            if (slices.Equal(sl, k)){
                j += 1
                break
            }
        }
        if j == 0{
            res = append(res, sl)
        }
        a++
        b--
    }
    }
}
return res
}
