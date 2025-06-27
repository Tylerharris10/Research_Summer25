import numpy as np
import matplotlib.pyplot as plt
import os


if __name__ == '__main__' : 

    file_save_path = os.path.join(os.getcwd(), 'Figures')
    os.makedirs(file_save_path, exist_ok=True)
    
    print("Hello World")

    a = np.array([4,5,6])

    fig = plt.figure(figsize=(12, 6))

    ax1 = fig.add_subplot(122)
    ax2 = fig.add_subplot(121)

    x = np.linspace(0, 2*np.pi, 100)
    y = np.sin(x)
    y2 = np.cos(x)

    ax1.plot(x, y, color='Navy', linestyle='dashed', alpha=0.9)
    ax1.set_xlabel('Angle x [Radians]')
    ax1.set_ylabel('f(x) = sin(x)')

    ax2.plot(x, y2, color='Red', linestyle='dashed', alpha=0.9)
    ax2.set_xlabel('Angle x [Radians]')
    ax2.set_ylabel('f(x) = cos(x)')

    fig.savefig(os.path.join(file_save_path, 'my_figure.png'), dpi=300)
    print('Hello')

