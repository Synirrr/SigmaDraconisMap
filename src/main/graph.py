from plotly import graph_objects as go
import numpy as np

class Grapher:
    def __init__(self):
        pass

    def spheres(self, size, clr, centre_x, centre_y, centre_z): 
    
        # Set up 100 points. First, do angles
        theta = np.linspace(0,2*np.pi,100)
        phi = np.linspace(0,np.pi,100)
        
        # Set up coordinates for points on the sphere
        x0 = size * np.outer(np.cos(theta),np.sin(phi)) + centre_x
        y0 = size * np.outer(np.sin(theta),np.sin(phi)) + centre_y
        z0 = size * np.outer(np.ones(np.size(theta)),np.cos(phi)) + centre_z
        
        # Set up trace
        trace = go.Surface(x=x0, y=y0, z=z0, colorscale=[[0,clr], [1,clr]])
        trace.update(showscale=False)

        return trace