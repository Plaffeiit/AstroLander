import astrolander as astro

def header_str():
    return f'{'TIME:SEC':^10}{'ALTITUDE:M':^15}{'VELOCITY:M/S2':^15}{'FUEL:KG':^15}{'THRUST:KG':^10}'

def data_str(lander: astro.Lander):
    return f'{int(time):^10}{lander.pos_y:^15.3f}{lander.speed_absolute():^15.3f}{lander.mass_fuel:^15.1f}?>'

if __name__ == '__main__':
    planet = astro.Planet()
    lander = astro.Lander()
    time = 0

    lander.acceleration = planet.gravity
    lander.set_position(0, 500)
    lander.set_speed(0, 30)
 
    lander.telemetry_append(time)
    
    print(header_str())
    while not lander.touchdown:
        set_thrust = input(data_str(lander))
        if not set_thrust.isnumeric():
            set_thrust = 0.0
        else:
            set_thrust = float(set_thrust)
        lander.thrust_set(set_thrust, 0)

        descent = astro.PhysicsEngine.descent_1d(lander, planet, planet.timetick)
        lander.speed_y, lander.acceleration = descent['speed_y'], descent['acceleration']
        position = astro.PhysicsEngine.position(lander, planet.timetick)
        lander.pos_y = position['y']
        lander.is_touchdown()
       
        time += planet.timetick
        lander.telemetry_append(time)
        
        lander.thrust_reset()

    print(data_str(lander))
    lander.telemetry_save()

''' #^ [1] Chat-GPT:
15264 kg - 8165 kg = 7099 kg (Masse des Landemoduls abzüglich Treibstoff Abstieg)
7099 kg * (1.625 kg/m2 // 9.807 kg/m2) = 1176 kg (Masse Landemodul auf dem Mond)
8165 kg * (1.625 kg/m2 // 9.807 kg/m2) = 1353 kg (Masse Abstieg-Treibstoff auf dem Mond)
'''