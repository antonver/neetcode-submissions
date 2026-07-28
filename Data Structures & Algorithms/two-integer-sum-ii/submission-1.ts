class Solution {
    /**
     * @param {number[]} numbers
     * @param {number} target
     * @return {number[]}
     */
    twoSum(numbers: number[], target: number): number[] {
        let a: number = 0;
        let b: number = numbers.length - 1;
        while (a < b){
            if (numbers[a] + numbers[b] < target){
                ++a
            }else if (numbers[a] + numbers[b] > target){
                --b
            }else{
                return [a + 1, b + 1];
            }
        }
        return [a,b];
    }
}
