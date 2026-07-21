class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices: number[]): number {
		let dif = 0;
		let min_ = prices[0];
		for (let i of prices.slice(1)){
			if (i-min_ > dif){
				dif = i - min_;
			}
			if (min_>i){
				min_ = i
			}
		}
		return dif;
	}
}
