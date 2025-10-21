import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact

def conic_section(alpha=45, beta=30):
    fig, ax = plt.subplots(figsize=(6,6))

   # Conditions you can refer to the images 

    if beta > alpha:
        # Hyperbola
        x = np.linspace(-3,3,400)
        y = np.sqrt((x**2)/(np.tan(np.radians(beta))**2) - 1)
        ax.plot(x, y, 'r')
        ax.plot(x, -y, 'r')
        ax.set_title("Hyperbola")
        
    elif beta == alpha:
        # Parabola
        x = np.linspace(-3,3,400)
        y = (x**2)/4
        ax.plot(x, y, 'r')
        ax.set_title("Parabola")
        
    elif beta < alpha and beta > 0:
        # Ellipse
        t = np.linspace(0, 2*np.pi, 400)
        a = 2
        b = a * np.cos(np.radians(beta))/np.cos(np.radians(alpha))
        x = a*np.cos(t)
        y = b*np.sin(t)
        ax.plot(x, y, 'r')
        ax.set_title("Ellipse")
        
    else:
        # Circle
        t = np.linspace(0, 2*np.pi, 400)
        r = 2
        ax.plot(r*np.cos(t), r*np.sin(t), 'r')
        ax.set_title("Circle")
    
    # Styling
    ax.set_aspect("equal")
    ax.axhline(0, color='k', lw=0.5)
    ax.axvline(0, color='k', lw=0.5)
    ax.grid(True, linestyle="--", alpha=0.5)
    ax.set_xlim(-3,3)
    ax.set_ylim(-3,3)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    
    plt.show()

# Interactive 2D view
interact(conic_section, alpha=(20,70,1), beta=(10,80,1))
