class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # V.2.0
        # Think about the two sorted array -> nums1 and nums2 
        # The left side count is always wil be the half of the total size of the array num1 and num2
        # also right side array is always <= left if not swap them  A , B = B , A like that 
        # then will we can able to find the solution :
        # median of the array will calculated in way like 
        # large element for me from the left side -> right most
        # smallest element form the right side -> left most
        # to find the efficientlly 
        # Binaery search will be on the small arrya 
        # Aleft <= Bright  and Bleft <= Aright 

        # A = [1,2,3,4,5]
        # B = [4 ,5 ,6 ,7 ,8 ,9 ,10 ,11]
        # Total = [1,2 ,3 ,4, 4, 5 , 5, 6 ,7 ,8 , 9 ,10 ,11 ] 
        # A , B = nums1 , nums2 
        # total = len(nums1) + len(nums2)
        # half = total // 2

        # if len(B) < len(A) :
        #     A , B = B , A 
        
        # # Bineary Search on the small array
        # l , r = 0 , len(A) - 1 
        # while True :
        #     i = (l + r) // 2
        #     j = half - i - 2 

        #     Aleft = A[i] if i >= 0 else float("-infinity")
        #     Aright = A[i+1] if (i + 1) < len(A) else float("infinity")
        #     Bleft = B[j] if j >= 0 else float("-infinity")
        #     Bright = B[j + 1] if (j + 1 ) < len(B) else float("infinity")

        #     # condition to check the its even or odd 
        #     if Aleft <= Bright and Bleft <= Aright :
        #         if total % 2 == 0  :
        #             return min(Aright , Bright)
        #         return (max(Aleft , Bleft) + min(Aright , Bright)) // 2

        #     elif Aleft > Bright :
        #             r = i - 1
        #     else :
        #             l = i + 1\

   
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1