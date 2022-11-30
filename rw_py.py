from random_walk import RandomWalk
import matplotlib.pyplot as plt
import os

while True:
    path = os.path.dirname(__file__)
    path_dir = os.path.join(path, 'ploted_images')
    sample_file_name = 'random_walk'
    os.makedirs(path_dir, exist_ok=True)
    rw = RandomWalk()
    rw.fill_walk()

    plt.style.use('classic')
    point = range(rw.points)
    fig, ax = plt.subplots(figsize=(15, 9))

    ax.scatter(rw.x_values, rw.y_values, c=point,
               cmap=plt.cm.Blues, edgecolors='none', s=15)

    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1],
               c='red', edgecolors='none', s=100)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    running = input("make another walk? y/n ")
    if running == 'n':
        break
    plt.savefig(os.path.join(path_dir, sample_file_name))
    plt.close()
