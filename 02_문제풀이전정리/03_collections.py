# ============================================================
# 알고리즘 자주 쓰는 collections 모듈
# ============================================================
from collections import deque, Counter, defaultdict, OrderedDict

# ------------------------------------------------------------
# deque - 양방향 큐 (BFS에서 필수)
# ------------------------------------------------------------

dq = deque([1, 2, 3])

dq.append(4)        # 오른쪽 삽입 → [1,2,3,4]
dq.appendleft(0)    # 왼쪽 삽입  → [0,1,2,3,4]
dq.pop()            # 오른쪽 제거 → 4 반환
dq.popleft()        # 왼쪽 제거  → 0 반환

# list vs deque 속도 차이
# list.pop(0)   → O(n) : 앞에서 제거할 때 전체 이동 발생
# deque.popleft → O(1) : BFS에서 list 대신 deque를 써야 하는 이유

# BFS 기본 구조
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()      # O(1)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

dq.rotate(1)        # 오른쪽으로 1칸 회전 [1,2,3] → [3,1,2]
dq.rotate(-1)       # 왼쪽으로 1칸 회전  [1,2,3] → [2,3,1]


# ------------------------------------------------------------
# Counter - 빈도 계산
# ------------------------------------------------------------

c = Counter("banana")       # {'a':3, 'n':2, 'b':1}
c = Counter([1, 2, 2, 3])   # {2:2, 1:1, 3:1}

c.most_common(2)            # [(2,2), (1,1)] | 상위 N개
c['a']                      # 3 | 없는 키는 0 반환 (KeyError 없음)

# 두 Counter 연산
c1 = Counter("aab")
c2 = Counter("abc")
c1 + c2     # Counter({'a':3, 'b':2, 'c':1}) | 합산
c1 - c2     # Counter({'a':1})               | 차집합 (0 이하 제거)
c1 & c2     # Counter({'a':2, 'b':1})        | 교집합 (최솟값)
c1 | c2     # Counter({'a':2, 'b':1, 'c':1}) | 합집합 (최댓값)


# ------------------------------------------------------------
# defaultdict - 기본값 있는 딕셔너리
# ------------------------------------------------------------

# 일반 dict: 없는 키 접근 시 KeyError
d = {}
# d['a'] += 1  # KeyError 발생

# defaultdict: 없는 키 접근 시 기본값 자동 생성
dd_int = defaultdict(int)       # 기본값 0
dd_int['a'] += 1                # {'a': 1}

dd_list = defaultdict(list)     # 기본값 []
dd_list['key'].append(1)        # {'key': [1]}

dd_set = defaultdict(set)       # 기본값 set()
dd_set['key'].add(1)

# 그래프 인접 리스트 구현에 자주 사용
graph = defaultdict(list)
edges = [(1,2), (1,3), (2,4)]
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)
# graph = {1:[2,3], 2:[1,4], 3:[1], 4:[2]}


# ------------------------------------------------------------
# OrderedDict - 삽입 순서 보장 딕셔너리
# ------------------------------------------------------------
# 파이썬 3.7+ 부터 일반 dict도 삽입 순서 보장
# 현재는 move_to_end 기능이 필요할 때만 사용

od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od.move_to_end('a')         # 'a'를 맨 뒤로
od.move_to_end('c', last=False)  # 'c'를 맨 앞으로
# LRU 캐시 구현에 활용
