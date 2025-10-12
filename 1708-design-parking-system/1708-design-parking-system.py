class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
       self.sanjna = {1 : big, 2: medium, 3: small}
        

    def addCar(self, carType: int) -> bool:
        self.sanjna[carType] -= 1
        return self.sanjna[carType] >= 0
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)