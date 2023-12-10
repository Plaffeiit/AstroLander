class LanderGame:
    def __init__(self):
        self.floor_height = 0.0  # meters
        self.ball_height = 100.0  # meters
        self.ball_velocity = 0.0 # meters per second
        self.timestep = 1.0  # seconds
        self.gravitational_constant = 1.6
        self.running = True

    def update_timestep(self):
        acceleration = -self.gravitational_constant
        accel_contribution = 0.5 * acceleration * self.timestep * self.timestep
        
        self.ball_height += self.ball_velocity * self.timestep
        self.ball_velocity += acceleration * self.timestep
        
        print(f'Ball is at {self.ball_height:.3f} m with {self.ball_velocity:.1f} m/s.')

        if self.ball_height <= self.floor_height:
            self.ball_height = self.floor_height
            print(f'The ball hits the floor with a thud.')
            self.running = False


game = LanderGame()

while game.running:
    game.update_timestep()
