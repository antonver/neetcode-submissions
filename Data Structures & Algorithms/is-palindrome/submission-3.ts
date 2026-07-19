class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s: string): boolean {
        let i = 0;
        let b = s.length - 1;
        while (i < b){
            while (i < b && !this.isAlphaNum(s[i])){
                i++
            }
            while (i < b && !this.isAlphaNum(s[b])){
                b--
            }
            if (i < b && s[i].toLowerCase() != s[b].toLowerCase()){
                return false
            }
            i++
            b--
            
        }
        return true
    }
    isAlphaNum(s: string): boolean{
        return /^[0-9A-Za-z]$/.test(s);
    }
}
