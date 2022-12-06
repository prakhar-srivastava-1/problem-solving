class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        # count number of zeroes
        zeros = arr.count(0)

        # length of arr
        len_arr = len(arr)

        # from where do we start
        idx = 0
        if zeros > 0 and len_arr != zeros:
            for i in range(zeros):
                idx = arr.index(0, idx)
                # split and insert duplicate zero
                arr[:] = arr[:idx] + [0, 0] + arr[idx+1:]
                idx += 2
            
            arr[:] = arr[:len_arr]