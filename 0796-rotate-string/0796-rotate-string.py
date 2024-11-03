class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        s_q = deque(s)
        g_q = deque(goal)

        for i in range(len(s)):
            if ''.join(s_q) == ''.join(g_q):
                return True
            s_q.append(s_q.popleft())

        return False