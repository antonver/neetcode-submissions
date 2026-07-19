func isPalindrome(s string) bool {
    i := 0
    b := len(s) - 1
    s = strings.ToLower(s)
    for i < len(s) && b >= 0{
        for i < len(s) && !unicode.IsLetter(rune(s[i])) && !unicode.IsDigit(rune(s[i])){
            i++
        }
        for b >= 0 && !unicode.IsLetter(rune(s[b])) && !unicode.IsDigit(rune(s[b])){
            b--
        }
        if i < len(s) && b >= 0 && s[i] != s[b]{
            return false
        }
        i++
        b--
    }
    return true
}
