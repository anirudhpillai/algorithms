def decodeString(self, s):
        clean = True
        for i in s:
            if i == '[' or i == ']':
                clean = False

        if clean:
            return s

        result = ""
        i = 0

        while i < len(s):
            if s[i] == '[':
                num = s[i-1]
                end = i
                while end < len(s):
                    if s[end] == ']':
                        break
                    end += 1
                result += int(num)*self.decodeString(s[i+1:end])
                i = end
            elif s[i] not in "]1234567890":
                result += s[i]

            i += 1

        return result
