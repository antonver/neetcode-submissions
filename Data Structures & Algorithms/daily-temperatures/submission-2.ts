class Solution {
    /**
     * @param {number[]} temperatures
     * @return {number[]}
     */
    dailyTemperatures(temperatures: number[]): number[] {
        let stack: number[] = [];
        let result: number[] = new Array(temperatures.length).fill(0);
        for (let i = 0; i < temperatures.length; i++){
            while (stack.length > 0 && temperatures[i] > temperatures[stack[stack.length - 1]]){
                let k = stack.pop();
                result[k] = i - k;
            } 
            stack.push(i);
        }
        return result;
    }
}
