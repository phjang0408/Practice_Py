scores = [int(input()) for _ in range(6)]
total = sum(scores)
percentages = [score / total * 100 for score in scores]

problem_idx = None
for idx, pct in enumerate(percentages):
    print(f"{idx + 1}: {pct:.3f}")
    if pct >= 30.0 and problem_idx is None:
        problem_idx = idx

if problem_idx is not None:
    print(f"Problem at {problem_idx + 1}")
    print(f"Result: {percentages[problem_idx]:.3f} %")
else:
    print("Fair")


# ===== 원본 코드 =====s`
# total = 0
# dic = {}
# li = []
# NotF=False
# for i in range(6):
#     x = int(input())
#     dic[i] = x
#     total += x
# for i in range(6):
#     li.append(dic[i] / total * 100)
# for x in range(6):
#     print("%d: %.3f"%(x+1, li[x]))
#     if li[x] >= 30.0:
#         NotF = True
#         target = x
#
# if NotF:
#     print(f"Problem at {target+1}")
#     print("Result: %.3f %%"%li[target])
# else:
#     print("Fair")