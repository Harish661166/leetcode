class Solution:
    def isValid(self, s: str) -> bool:

        brace_map = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        stack = []

        for brace in s:

            if brace in brace_map:
                stack.append(brace)
            else:

                if not stack or brace != brace_map[stack.pop()]:
                    return False

        return len(stack) == 0