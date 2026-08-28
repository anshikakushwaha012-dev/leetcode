class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        count = [0] * 26

        # Count characters
        for ch in s:
            count[ord(ch) - ord('a')] += 1

        # A palindrome can have at most one odd frequency
        odd = 0
        middle = ""

        for i in range(26):
            if count[i] % 2 == 1:
                odd += 1
                middle = chr(ord('a') + i)

        if odd > 1:
            return ""

        # Characters available for the left half
        half_count = [x // 2 for x in count]

        prefix = []

        def possible():
            # Build the largest possible completion
            left = "".join(prefix)

            for i in range(25, -1, -1):
                left += chr(ord('a') + i) * half_count[i]

            palindrome = left + middle + left[::-1]

            return palindrome > target

        # Build the smallest valid left half
        for _ in range(len(s) // 2):

            for i in range(26):

                if half_count[i] == 0:
                    continue

                # Try this character
                half_count[i] -= 1
                prefix.append(chr(ord('a') + i))

                if possible():
                    break

                # Undo if it cannot work
                prefix.pop()
                half_count[i] += 1

            else:
                return ""

        left = "".join(prefix)

        answer = left + middle + left[::-1]

        return answer if answer > target else ""