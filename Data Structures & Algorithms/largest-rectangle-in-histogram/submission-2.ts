class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    largestRectangleArea(heights: number[]): number {
        let stack: number[] = [];
        let left = -1;
        let max_area = 0;
        let height = 0;
        let width = 0;
        heights.push(0);
        for (const [i, h] of heights.entries()){
            while (stack.length > 0 && heights[stack[stack.length - 1]] > h){
                height = heights[stack.pop()];
                left = stack.length > 0 ? stack[stack.length - 1] : -1;
                width = height * (i - left - 1);
                max_area = Math.max(max_area, width);
            }
            stack.push(i);
        }
        return max_area;
    }
}
