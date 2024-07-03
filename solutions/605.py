class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerLen = len(flowerbed) 
        if flowerLen == 0: 
            return False

        counter = 0 
        for i in range(flowerLen):
            if flowerbed[i] == 0:     
                empty_left_plot = (i == 0) or (flowerbed[i - 1] == 0)
                empty_right_plot = (i == flowerLen - 1) or (flowerbed[i + 1] == 0) 

                if empty_left_plot and empty_right_plot: 
                    flowerbed[i] = 1 
                    counter += 1
                    if counter >= n: 
                        return True
        
        return counter >= n 