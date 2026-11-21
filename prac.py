class Cars:
    # class attribute
    num_of_wheels = 4

    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def start_car(self):
        self.num_of_wheels = 8
        return "Car has started"
    def stop_car(self):
        return "Car has stopped"

# Creating objects 
bmw = Cars(color="Black", mileage=10000)
# If we put this here it modifies the num of wheels to be 10
# Cars.num_of_wheels = 10
print(bmw.num_of_wheels)
print(bmw.start_car())
print(bmw.color)