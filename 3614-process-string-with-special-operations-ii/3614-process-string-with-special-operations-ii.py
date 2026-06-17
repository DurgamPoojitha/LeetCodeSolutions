class Solution:
    def processStr(self, s, k):
        n = len(s)

        lengths = [0] * (n + 1)

        for i, ch in enumerate(s):
            cur = lengths[i]

            if 'a' <= ch <= 'z':
                lengths[i + 1] = cur + 1

            elif ch == '*':
                lengths[i + 1] = max(0, cur - 1)

            elif ch == '#':
                lengths[i + 1] = cur * 2

            elif ch == '%':
                lengths[i + 1] = cur

        if k >= lengths[n]:
            return '.'

        for i in range(n - 1, -1, -1):
            ch = s[i]

            before = lengths[i]
            after = lengths[i + 1]

            if 'a' <= ch <= 'z':
                if k == after - 1:
                    return ch

            elif ch == '#':
                if k >= before:
                    k -= before

            elif ch == '%':
                if after > 0:
                    k = after - 1 - k

            elif ch == '*':
                pass

        return '.'