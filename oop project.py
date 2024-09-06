# project: vehicle managment system
#description : create a pgm that manages different types of vehicles,including cars, trucks,and motorcycles.each vehicle
#  should have attributes such as brand,model,year and color.the pgm should also include methods to start engine,accelerate
#  and brake.



#parent class:vehicle

class Vehicle:
    def __init__(self,brand,model,year,color):
        self.brand=brand
        self.model=model
        self.year=year
        self.color=color
    def start_engine(self):
        print('vroom!')
    def accelerate(self):
        print('Accelerating...')
    def brake(self):
        print('Braking...')

#chlld classes
#car classes

class Car(Vehicle):
    def __init__(self,brand,model,year,color,num_doors):# here num doors =attributes
        super().__init__(brand,model,year,color)#super() is used to call parent function 
        self.num_doors=num_doors
    def open_trunk(self):
        print('Trunk opened!')#open trunk is method

#trunk class

class Trunk(Vehicle):
    def __init__(self,brand,model,year,color,cargo_capacity):
        super().__init__(brand,model,year,color)
        self.cargo_capacity=cargo_capacity
    def load_cargo(self):
        print('LOADING CARGO...')#method of trunk



#MOTOR CYCLE CLASS

class Motorcycle(Vehicle):
    def __init__(self,brand,model,year,color,engine_size):
        super().__init__(brand,model,year,color)
        self.engine_size=engine_size
    def wheelie(self):
        print('Doing a wheelie')# method of mc



#main program:
def main():
    car=Car('Toyota','corolla',2015,'blue',4)#here we create object Car is object and in () its parameter 
    trunk=Trunk('ford','f-150',2018,'red',1000)
    motorcycle=Motorcycle('harley_davidson','electra glide',2020,'black',1200)

    car.start_engine()# access method inside class
    car.accelerate()
    car.brake()
    car.open_trunk()


    trunk.start_engine()
    trunk.accelerate()
    trunk.brake()
    trunk.load_cargo()


    motorcycle.start_engine()
    motorcycle.accelerate()
    motorcycle.brake()
    motorcycle.wheelie()


if __name__=='__main__':
    main()













