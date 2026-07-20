class Solution {
    /**
     * @param {number} target
     * @param {number[]} position
     * @param {number[]} speed
     * @return {number}
     */
    carFleet(target: number, position: number[], speed: number[]): number {
		let stack: number[][] = [];
		let fleet = 0;
		let min_time: number = 0.0;
		for (let i = 0; i < position.length; i++){
			stack.push([position[i], speed[i]]);
		}
		stack.sort((a,b) => b[0] - a[0]);
		for (let [p, s] of stack){
			let t = (target - p) / s;
			if (t > min_time){
				fleet += 1;
				min_time = t;
			}
		}
		return fleet;

	}


}
