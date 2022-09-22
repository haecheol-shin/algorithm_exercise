import sys;

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
dap = [-1] * n
idx = []
st = []
for i in range(n - 1):
    if nums[i] > nums[i + 1]:
        st.append(nums[i])
        idx.append(i)
    else:
        dap[i] = nums[i + 1]
        if len(st) != 0 and st[-1] < nums[i + 1]:
            while st and st[-1] < nums[i + 1]:
                dap[idx[-1]] = nums[i + 1]
                st.pop()
                idx.pop()
print(*dap)