import time
import random
from abc import ABC, abstractmethod


class CarInterface(ABC):
    @abstractmethod
    def gas(self):
        return print("Speed up")

    @abstractmethod
    def brake(self):
        return print("Speed down")


class EngineInterface(ABC):
    @abstractmethod
    def start(self):
        return print("Engine ON")

    @abstractmethod
    def stop(self):
        return print("Engine OFF")


class AutopilotLightsInterface(ABC):
    @abstractmethod
    def traffic_lights(self):
        return print("green")


class AutopilotCarsInterface(ABC):
    @abstractmethod
    def front_cars(self):
        return print("no car in front")


class Car(CarInterface):
    speed = 0

    @staticmethod
    def gas(**kwargs):
        Car.speed += 5
        print(Car.speed, "km/h Speed Up")
        return Car.speed

    @staticmethod
    def brake(**kwargs):
        Car.speed -= 10
        if Car.speed < 0:
            Car.speed = 0
        print(Car.speed, 'km/h Speed down')
        return Car.speed

    @staticmethod
    def get_speed():
        return Car.speed


class Engine(EngineInterface):
    engine_status = "OFF"

    @staticmethod
    def start(**kwargs):
        Engine.engine_status = 'ON'
        print("Start engine")

    @staticmethod
    def stop(**kwargs):
        Engine.engine_status = 'OFF'
        print("Engine stop")


class Autopilot(AutopilotCarsInterface, AutopilotLightsInterface):
    traffic_light = "green"
    front_car = False

    @staticmethod
    def front_cars(**kwargs):
        chance = random.randint(0, 101)
        if chance < 30:
            Autopilot.front_car = True
            print("Warning, car in front of you, max speed is 30 km/h")
        else:
            Autopilot.front_car = False
        return Autopilot.front_car

    @staticmethod
    def traffic_lights(**kwargs):
        chance = random.randint(0, 101)
        if chance < 10:
            Autopilot.traffic_light = "red"
            print("Warning, traffic light is RED, lowering the speed")
        else:
            Autopilot.traffic_light = 'green'
        return Autopilot.traffic_light


Engine.start()

while True:
    time.sleep(1)
    if not Autopilot.front_car:
        print("No cars in front of you")
        if Autopilot.traffic_light == "green":
            print("Traffic light is green")
            time.sleep(1)
            if Engine.engine_status == "OFF":
                Engine.start()
                time.sleep(1)
            if Car.speed < 60:
                Car.gas()
                time.sleep(1)
            else:
                print(Car.speed, "km/h")
                time.sleep(1)
        else:
            while Car.speed > 0:
                Car.brake()
                time.sleep(1)
            Engine.stop()
            time.sleep(1)
    else:
        if Car.speed > 30:
            while Car.speed > 30:
                Car.brake()
                time.sleep(1)
        else:
            if Car.speed < 30:
                Car.gas()
                time.sleep(1)

    Autopilot.traffic_lights()
    Autopilot.front_cars()
