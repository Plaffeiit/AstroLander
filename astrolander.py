import math

class Lander():
    def __init__(self):
        self.name = 'Eagle'  # name of lander
        self.mass_empty = 1176  #^ [kg] mass of lander without descent fuel[1]
        self.mass_fuel = 1353  #^ [kg] mass of descent fuel[1]
        self.pos_x = 0 # TODO: [m] x position (horizontal)
        self.pos_y = 1000 # [m] y position (Altitude)
        self.speed_x = 0 # TODO: [m/s] speed horizontal
        self.speed_y = 0 # [m/s] speed vertical
        self.acceleration = 0  # [m/s2]
        self.thrust = 0 # [N, kg*m/s2] thrust
        self.thrust_dir = 0 # TODO: [deg] thrust direction (0 = down)
        self.touchdown = False  # [bool] True if lander touches ground
        self.telemetry = ['time,mass_total,pos_x,pos_y,acceleration,speed_x,speed_y,speed_abs,mass_fuel,thrust,thrust_dir']

    def __str__(self):
        return f'{self.name}, Mass {self.mass_total()} kg, Altitude {self.pos_y} m, Speed {self.speed_absolute()} m/s'
    
    # Gibt die absolute Geschwindigkeit des Landers zurück
    def speed_absolute(self) -> float:
        return math.sqrt(self.speed_x**2 + self.speed_y**2)
    
    # Gibt das Gesamtgewicht des Landers zurück
    def mass_total(self) -> float:
        return self.mass_empty + self.mass_fuel
    
    def thrust_set(self, thrust: float, thrust_dir: float):
        if thrust < self.mass_fuel:
            self.thrust = thrust
        else:
            self.thrust = self.mass_fuel
        
        self.thrust_dir = thrust_dir  #TODO: check if thrust_dir is in range 0-360

    def thrust_reset(self):
        self.mass_fuel -= self.thrust
        self.thrust = 0
        self.thrust_dir = 0

    def set_position(self, x: int, y: int):
        self.pos_x = x
        if y >= 0:
            self.pos_y = y
        else:
            self.pos_y = 0

    def set_speed(self, x: int, y: int):
        self.speed_x = x
        if y <= 0:
            self.speed_y = y
        else:
            self.speed_y = -y

    def is_touchdown(self) -> bool:
        if self.pos_y <= 0:
            self.pos_y = 0
            self.touchdown = True
        return self.touchdown
    
    def telemetry_append(self, time: float = None):
        tm_data = ','.join(map(str, [time, self.mass_total(), self.pos_x, self.pos_y, self.acceleration, self.speed_x, self.speed_y, self.speed_absolute(), self.mass_fuel, self.thrust, self.thrust_dir]))
        self.telemetry.append(tm_data)
    
    def telemetry_save(self, file: str = 'lander_telemetry.csv'):
        with open(file, 'w') as f:
            for line in self.telemetry:
                f.write(line + '\n')
            f.close()

class Planet():
    def __init__(self):
        self.name = 'Luna'  # name of planet
        self.gravity = self.gravity_moon()  # [m/s2]
        self.atmosphere = 0  # TODO: [kg/m3] atmosphere (0 = no atmosphere)
        self.wind = 0  # TODO: [m/s] wind speed and x diretion (0 = no wind)
        self.timetick = 1.0  # [s] time tick for physics engine
        # TODO: self.Landing_size (1 = size of the lander)
    
    def __str__(self):
        return f'{self.name}, Gravity {self.gravity} m/s2, Atmosphere {self.atmosphere} kg/m3, Wind {self.wind} m/s'

    @staticmethod
    def gravity_earth() -> float:
        return 9.807  # [m/s2] gravity on earth   
    @staticmethod
    def gravity_moon() -> float:
        return 1.625  # [m/s2] gravity on moon

class PhysicsEngine:
    @staticmethod
    def descent_1d(lander: Lander, planet: Planet, tick_sec: float = 1.0) -> float:
        acceleration = planet.gravity - 100 * (lander.thrust / lander.mass_total())
        speed_y = lander.speed_y + (0.5 * (-acceleration) * tick_sec**2)
        return {'speed_x': 0.0, 'speed_y': speed_y, 'acceleration': acceleration}
    
    @staticmethod
    def descent_2d(lander: Lander, planet: Planet, tick_sec: float = 1.0) -> float:
        # return {'speed_x': speed_x, 'speed_y': speed_y, 'acceleration': acceleration}
        pass
    
    @staticmethod
    def position(lander: Lander, tick_sec: float = 1.0) -> float:
        px = lander.pos_x + lander.speed_x * tick_sec
        py = lander.pos_y + lander.speed_y * tick_sec
        return {'x': px, 'y': py}