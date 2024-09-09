
class Water_Trap:
    def __init__(self,Height):
        if not isinstance(Height,list) or not all(isinstance(element,int) and element >=0 for element in Height):
            raise ValueError("Height must be a list of non-negative integers.")
        self.height = Height
        """
        Documentation: Initializing a class 'Water_Trap' with a validated map as a list 'Height' ensuring that the list
         contains non-negative integers. 
        """

    def count(self):
        n=len(self.height)
        water_unit=0
        left_max=[0]*n
        right_max=[0]*n

        left_max[0]=self.height[0]
        for i in range(1,n):
            left_max[i]=max(self.height[i],left_max[i-1])

        right_max[n-1]=self.height[n-1]
        for i in range(n-2,-1,-1):
            right_max[i]=max(self.height[i],right_max[i+1])

        for i in range(n):
            water_unit+=min(left_max[i],right_max[i])-self.height[i]

        return water_unit
    """
    Documentation: A class function 'count' calculating the amount of water units trapped in between the 
    height blocks (represented as each element of list 'Height').
    """

height=[2,3,1,4]
water_trapped=Water_Trap(height)
print(water_trapped.count())

