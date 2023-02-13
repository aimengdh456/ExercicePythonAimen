import threading
import time

MAX_TANK_CAPACITY = 50
current_oil = 0
nb_wheels = 0
nb_motors = 0

class Pump:
    def __init__(self, period, execution_time, production, name):
        self.period = period
        self.execution_time = execution_time
        self.production = production
        self.name = name
        self.thread = threading.Thread(target=self.run)

    def run(self):
        while True:
            global current_oil
            if current_oil + self.production <= MAX_TANK_CAPACITY:
                time.sleep(self.period)
                print(f"{self.name} started")
                time.sleep(self.execution_time)
                current_oil += self.production
                print(f"{self.name} produced {self.production} oil")
            else:
                print(f"{self.name} couldn't produce any oil because the tank is full")

class Machine:
    def __init__(self, period, execution_time, oil_consumption, nb_products, name):
        self.period = period
        self.execution_time = execution_time
        self.oil_consumption = oil_consumption
        self.nb_products = nb_products
        self.name = name
        self.thread = threading.Thread(target=self.run)

    def run(self):
        global current_oil, nb_wheels, nb_motors
        while True:
            time.sleep(self.period)
            if self.name == "Machine 1" and nb_wheels // 4 > nb_motors:
                print(f"{self.name} didn't produce any motor because there are already more motors than wheels")
            elif self.name == "Machine 2" and nb_wheels // 4 < nb_motors:
                print(f"{self.name} didn't produce any wheel because there are already more wheels than motors")
            else:
                if current_oil >= self.oil_consumption:
                    print(f"{self.name} started")
                    time.sleep(self.execution_time)
                    current_oil -= self.oil_consumption
                    if self.name == "Machine 1":
                        nb_motors += self.nb_products
                        print(f"{self.name} produced {self.nb_products} motor(s)")
                    elif self.name == "Machine 2":
                        nb_wheels += self.nb_products
                        print(f"{self.name} produced {self.nb_products} wheel(s)")
                else:
                    print(f"{self.name} couldn't start because there isn't enough oil in the tank")

if __name__ == "__main__":
    pump1 = Pump(5, 2, 10, "Pump 1")
    pump2 = Pump(15, 3, 20, "Pump 2")
    machine1 = Machine(5, 5, 25, 1, "Machine 1")
    machine2 = Machine(5, 3, 5, 4, "Machine 2")

    pump1.thread.start()
    pump2.thread.start()
    machine1.thread.start()
    machine2.thread.start()
