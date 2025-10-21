import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from ipywidgets import interact

def cone_with_plane(alpha=45, beta=30):
    fig = plt.figure(figsize=(6,6))
    ax3d = fig.add_subplot(111, projection='3d')
    
    # Put then Cone parameters however u like

    h = 3
    r = np.tan(np.radians(alpha)) * h
    theta = np.linspace(0, 2*np.pi, 60)
    z = np.linspace(0, h, 40)
    T, Z = np.meshgrid(theta, z)
    X = (Z/h)*r*np.cos(T)
    Y = (Z/h)*r*np.sin(T)
    
    # Upper and lower part of the cone

    ax3d.plot_surface(X, Y, Z, color="orange", alpha=0.6, edgecolor='k')
    ax3d.plot_surface(X, Y, -Z, color="orange", alpha=0.6, edgecolor='k')

    # Plane part 

    size = 3
    xx = np.array([[-size, size, size, -size]])
    yy = np.array([[-size, -size, size, size]])
    zz = np.tan(np.radians(beta)) * yy
    verts = [list(zip(xx[0], yy[0], zz[0]))]
    plane = Poly3DCollection(verts, alpha=0.3, facecolor='cyan', edgecolor='k')
    ax3d.add_collection3d(plane)

    
    ax3d.set_xlim(-3,3)
    ax3d.set_ylim(-3,3)
    ax3d.set_zlim(-3,3)
    ax3d.view_init(elev=20, azim=30)
    ax3d.set_title("Cone + Cutting Plane")
    ax3d.set_axis_off()
    
    plt.show()

# Interactive 3D view
interact(cone_with_plane, alpha=(20,70,1), beta=(10,80,1))
