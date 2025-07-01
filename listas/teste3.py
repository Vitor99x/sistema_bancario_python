def ranks(arr):
    # Write your code here
    sorted_unique = sorted(set(arr), reverse=True)

    rank_dict = {v: i + 1 for i, v in enumerate(sorted_unique)}

    return [rank_dict[v] for v in arr]
 sorted
    pass

n = int(input())
arr = list(map(int, input().split()))

out_ = ranks(arr)
print (' '.join(map(str, out_)))