from random import choice
import os
class RandomWalk:
    def __init__(self, points=5000):
        self.points = points
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        while len(self.x_values) < self.points:
            x_direction = choice([-1, 1])
            x_distance = choice([0, 1, 2, 3, 4, 5, 6])
            y_direction = choice([-1, 1])
            y_distance = choice([0, 1, 2, 3, 4, 5, 6])
            x_step = x_direction*x_distance
            y_step = y_direction*y_distance
            if x_step and y_step == 0:
                continue

            x = self.x_values[-1]+x_step
            y = self.y_values[-1]+y_step

            self.x_values.append(x)
            self.y_values.append(y)

    def save_into_path(self, filename, plt):
        path = os.path.dirname(__file__)
        path_dir = os.path.join(path, 'ploted_images')
        os.makedirs(path_dir, exist_ok=True)
        plt.savefig(os.path.join(path_dir, filename))
