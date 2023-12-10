import math

class Lander():
    def __init__(self):
        self.name = 'Eagle'  # [string] name of lander
        self.mass_empty = 1176  #^ [kg] mass of lander without descent fuel[1]
        self.mass_fuel = 1353  #^ [kg] mass of descent fuel[1]
        self.pos_x = 0 # TODO: [m] x position (horizontal)
        self.pos_y = 10000 # [m] y position (Altitude)
        self.speed_x = 0 # TODO: [m/s] speed horizontal
        self.speed_y = 0 # [m/s] speed vertical
        self.acceleration = 0  # [m/s2]
        self.thrust = 0 # [N, kg*m/s2] thrust
        self.thrust_dir = 0 # TODO: [deg] thrust direction (0 = down)
        self.telemetry = ['time,mass_total,pos_x,pos_y,speed_x,speed_y,speed_abs,mass_fuel,thrust,thrust_dir,acceleration']

    def __str__(self):
        return f'{self.name}, Mass {self.mass_total()} kg, Position ({self.pos_x}, {self.pos_y}) m, Speed {self.speed_absolute()} m/s'
    
    # Gibt die absolute Geschwindigkeit des Landers zurück
    def speed_absolute(self) -> float:
        return math.sqrt(self.speed_x**2 + self.speed_y**2)
    
    # Gibt das Gesamtgewicht des Landers zurück
    def mass_total(self) -> float:
        return self.mass_empty + self.mass_fuel
    
    def set_altitude(self, alt: int = 1000):
        self.pos_y = alt

    def touchdown(self) -> bool:
        if self.pos_y <= 0:
            self.pos_y = 0
            return True
        else:
            return False
    
class Planet():
    def __init__(self):
        self.name = 'Luna'  # [string] name of planet
        self.gravity = 1.625  # [m/s2] gravity
        self.atmosphere = 0  # TODO: [kg/m3] atmosphere (0 = no atmosphere)
        self.wind = 0  # TODO: [m/s] wind speed and x diretion (0 = no wind)
        self.timetick = 1.0  # [s] time tick for physics engine
        # TODO: self.Landing_size (1 = size of the lander)
    
    def __str__(self):
        return f'{self.name}, Gravity {self.gravity} m/s2, Atmosphere {self.atmosphere} kg/m3, Wind {self.wind} m/s'

    def gravity_earth() -> float:
        return 9.807  # [m/s2] gravity on earth

class PhysicsEngine:
    @staticmethod
    def descent(lander: Lander, planet: Planet, tick_sec: float = 1.0) -> float:
        return lander.speed_y + 0.5 * lander.acceleration * tick_sec**2


if __name__ == '__main__':
    planet = Planet()
    lander = Lander()
    time = 0

    lander.acceleration = planet.gravity
    lander.set_altitude(10000)  # [m]

    print(f'Planet: {planet}\nLander: {lander}\n')  # DEBUG: print planet and lander
 
    while lander.touchdown() == False:
        lander.speed_y = PhysicsEngine.descent(lander, planet, planet.timetick)
        lander.pos_y -= lander.speed_y * planet.timetick
        lander.thrust = 0

        time += planet.timetick
 

'''
#^ [1] Chat-GPT:
15264 kg - 8165 kg = 7099 kg (Masse des Landemoduls abzüglich Treibstoff Abstieg)
7099 kg * (1.625 kg/m2 // 9.807 kg/m2) = 1176 kg (Masse Landemodul auf dem Mond)
8165 kg * (1.625 kg/m2 // 9.807 kg/m2) = 1353 kg (Masse Abstieg-Treibstoff auf dem Mond)
'''