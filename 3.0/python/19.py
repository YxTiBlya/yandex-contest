N = int(input())
heap = []

for i in range(N):
    cmd = list(map(int, input().split()))
    
    if cmd[0] == 0:
        heap.append(cmd[1])
        pos = len(heap) - 1
        while pos > 0 and heap[pos] > heap[(pos-1)//2]:
            heap[pos], heap[(pos-1)//2] = heap[(pos-1)//2], heap[pos]
            pos = (pos-1)//2

    else:
        ans = heap[0]
        heap[0] = heap[-1]
        pos = 0
        while pos * 2 + 2 < len(heap):
            max_son_i = pos * 2 + 1
            if heap[max_son_i] < heap[max_son_i+1]:
                max_son_i += 1
            if heap[pos] < heap[max_son_i]:
                heap[pos], heap[max_son_i] = heap[max_son_i], heap[pos]
                pos = max_son_i
            else:
                break
        heap.pop()
        print(ans)
