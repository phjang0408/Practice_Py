# ============================================================
# 알고리즘 자주 쓰는 heapq, bisect 모듈
# ============================================================

# ------------------------------------------------------------
# heapq - 우선순위 큐 (최소 힙)
# ------------------------------------------------------------
import heapq

# 기본 사용
heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)
heapq.heappop(heap)     # 1 (가장 작은 값)
heapq.heappop(heap)     # 2
# 항상 최솟값이 heap[0]에 위치

# 리스트를 힙으로 변환
arr = [3, 1, 4, 1, 5]
heapq.heapify(arr)      # O(n) | arr 자체가 힙이 됨

# 최댓값 힙 (음수로 저장)
max_heap = []
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -1)
heapq.heappush(max_heap, -5)
max_val = -heapq.heappop(max_heap)  # 5

# 튜플로 우선순위 지정 (첫 번째 원소 기준 정렬)
task_heap = []
heapq.heappush(task_heap, (2, "task B"))
heapq.heappush(task_heap, (1, "task A"))
heapq.heappush(task_heap, (3, "task C"))
priority, task = heapq.heappop(task_heap)  # (1, "task A")

# 다익스트라 기본 구조
def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    heap = [(0, start)]    # (거리, 노드)

    while heap:
        cost, node = heapq.heappop(heap)
        if cost > dist[node]:
            continue
        for neighbor, weight in graph[node]:
            new_cost = cost + weight
            if new_cost < dist[neighbor]:
                dist[neighbor] = new_cost
                heapq.heappush(heap, (new_cost, neighbor))
    return dist

# nlargest / nsmallest
data = [3, 1, 4, 1, 5, 9, 2, 6]
heapq.nlargest(3, data)     # [9, 6, 5] | 상위 3개
heapq.nsmallest(3, data)    # [1, 1, 2] | 하위 3개


# ------------------------------------------------------------
# bisect - 이진 탐색 (정렬된 리스트에서 사용)
# ------------------------------------------------------------
import bisect

arr = [1, 3, 3, 5, 7]

# 삽입 위치 탐색 (O(log n))
bisect.bisect_left(arr, 3)   # 1 | 3이 들어갈 가장 왼쪽 인덱스
bisect.bisect_right(arr, 3)  # 3 | 3이 들어갈 가장 오른쪽 인덱스
bisect.bisect(arr, 3)        # 3 | bisect_right와 동일

# 정렬 유지하며 삽입
bisect.insort_left(arr, 4)   # arr = [1,3,3,4,5,7]
bisect.insort(arr, 6)        # arr = [1,3,3,4,5,6,7]

# 활용: 정렬 리스트에서 값 존재 여부 O(log n) 확인
def exists(arr, val):
    i = bisect.bisect_left(arr, val)
    return i < len(arr) and arr[i] == val

# 활용: 특정 값 이하의 원소 개수
def count_le(arr, val):
    return bisect.bisect_right(arr, val)  # val 이하인 원소 수

# 활용: 특정 범위 원소 개수 (lo <= x <= hi)
def count_range(arr, lo, hi):
    return bisect.bisect_right(arr, hi) - bisect.bisect_left(arr, lo)

arr = [1, 2, 3, 4, 5, 6]
count_range(arr, 2, 5)  # 4 (2,3,4,5)
