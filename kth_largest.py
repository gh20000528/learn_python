class Soltion:
    def findKthLargest(self, nums: List[int], k:int):
        # sift_down
        def sift_down(heap, i, n):
            while True:
                largest = i
                left = 2 * i + 1
                right = 2 * i + 2

                if left < n and heap[left] > heap[largest]:
                    largest = left
                if right < n and heap[right] > heap[largest]:
                    largest = right    
                if largest != i:
                    heap[i] ,heap[largest] = heap[largest], heap[i]
                    i = largest
                else:
                    break

        # build max heap
        n = len(nums)
        for i in range((n - 2) // 2, -1, -1):
            sift_down(nums, i, n)
        
        # pop  k 次
        size = n
        for _ in range(k):
            nums[0], nums[size - 1] = nums[size - 1], nums[0]
            ans = nums[size - 1]
            size -= 1
            sift_down(nums, 0, size)
        
        return ans