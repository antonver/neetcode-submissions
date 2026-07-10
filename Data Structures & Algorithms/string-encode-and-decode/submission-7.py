class Solution:

    def encode(self, strs: list[str]) -> str:
        l = [str(len(strs))] + [str(len(i)) for i in strs]
        l = " ".join(l)
        l = str(len(l)) + " " + l
        return l + "".join(strs)
    def decode(self, s: str) -> list[str]:
        length_of_substring = ""
        counter = 0
        for i in s:
            if i == " ":
                counter += 1
                break
            counter += 1
            length_of_substring += i
        length_of_substring = int(length_of_substring)
        lengths = [int(i) for i in s[counter:length_of_substring + counter].split(" ")]
        elements_num = lengths[0]
        lengths = lengths[1:]
        words = s[length_of_substring+counter:]
        res = []
        i = 0
        y = 0
        while y < elements_num:
            leng = lengths[y]
            if leng == 0:
                res += [""]
                y += 1
                continue
            res += [words[i:i+leng]]
            i += leng
            y += 1
        return res