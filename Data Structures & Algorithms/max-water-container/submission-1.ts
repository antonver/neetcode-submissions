class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights: number[]): number {
        let max_area = 0;
        let a = 0;
        let b = heights.length - 1;
        while (a<b){
            max_area = Math.max((Math.min(heights[a], heights[b]) * (b-a)), max_area)
            if (heights[a] <= heights[b]){
                ++a
                continue
            } 
            --b
        }
        return max_area;
    }
}
