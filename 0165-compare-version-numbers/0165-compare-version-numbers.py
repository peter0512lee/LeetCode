class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")

        len_v1, len_v2 = len(v1), len(v2)
        idx_v1 = idx_v2 = 0

        while (idx_v1 < len_v1 or idx_v2 < len_v2):
            revision1 = int(v1[idx_v1]) if (idx_v1 < len_v1) else 0
            revision2 = int(v2[idx_v2]) if (idx_v2 < len_v2) else 0

            if (revision1 < revision2): return -1
            if (revision1 > revision2): return 1

            idx_v1 += 1
            idx_v2 += 1

        return 0