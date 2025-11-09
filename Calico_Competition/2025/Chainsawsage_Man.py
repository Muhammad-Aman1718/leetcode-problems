# Chainsawsage Man


import sys


def solve():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    T = int(next(it))
    out_lines: list[str] = []
    for _ in range(T):
        N = int(next(it))
        K = int(next(it))
        H = [int(next(it)) for _ in range(N)]
        L = [int(next(it)) for _ in range(N)]

        maxH = max(H) if N > 0 else 0

        # coverage[x] counts links in interval [x, x+1)
        coverage = [0] * (maxH + 1)  # we use indices 0..maxH-1, extra slot safe
        for l, h in zip(L, H):
            # increment coverage on [l, h-1]
            if l < h:
                coverage[l] += 1
                coverage[h] -= 1  # we'll prefix-sum this difference array

        # convert difference array to actual coverage
        for i in range(1, maxH):
            coverage[i] += coverage[i - 1]

        # Build prefix pref[p] = sum coverage[0..p-1], for p in 0..maxH
        pref = [0] * (maxH + 1 + 0)  # pref length = maxH+1
        for p in range(1, maxH + 1):
            pref[p] = pref[p - 1] + coverage[p - 1]

        # We want pref[j] - pref[i] == K with 0 <= i < j <= maxH
        seen = {0: 0}  # map prefix value -> earliest index i
        found = False
        for j in range(1, maxH + 1):
            want = pref[j] - K
            if want in seen:
                i = seen[want]
                # output c1 i and c2 j (any order ok)
                out_lines.append(f"{i} {j}")
                found = True
                break
            # store prefix value earliest index
            if pref[j] not in seen:
                seen[pref[j]] = j

        if not found:
            out_lines.append("IMPOSSIBLE")

    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    solve()
