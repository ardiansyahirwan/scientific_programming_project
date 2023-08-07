import random
import copy


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            return self.contents
        drawn_balls = random.sample(self.contents, num_balls)
        for ball in drawn_balls:
            self.contents.remove(ball)
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0

    for _ in range(num_experiments):
        drawn_hat = copy.deepcopy(hat)
        drawn_balls = drawn_hat.draw(num_balls_drawn)
        
        # Check if expected balls are in the drawn balls
        success = all(drawn_balls.count(ball) >= count for ball, count in expected_balls.items())
        if success:
            success_count += 1
    
    probability = success_count / num_experiments
    return probability