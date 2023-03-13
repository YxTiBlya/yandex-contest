import sys
N = int(sys.stdin.readline())
heap = list(map(int, sys.stdin.readline().split()))
lwc = (N-2)//2 

for i in range(lwc, -1, -1):
    pos = i
    while pos * 2 + 1 < N:
        max_son_i = pos * 2 + 1
        if max_son_i + 1 < N and heap[max_son_i] < heap[max_son_i+1]:
            max_son_i += 1
        if heap[pos] < heap[max_son_i]:
            heap[pos], heap[max_son_i] = heap[max_son_i], heap[pos]
            pos = max_son_i
        else:
            break

j = -1
for i in range(N):
    ans = heap[0]
    heap[0] = heap[j]
    pos = 0
    while pos * 2 + 1 < N + j:
        max_son_i = pos * 2 + 1
        if max_son_i + 1 < N and heap[max_son_i] < heap[max_son_i+1]:
            max_son_i += 1
        if heap[pos] < heap[max_son_i]:
            heap[pos], heap[max_son_i] = heap[max_son_i], heap[pos]
            pos = max_son_i
        else:
            break

    heap[j] = ans
    j -= 1

print(*heap)