import numpy as np
import plotly.graph_objects as go

# Helper function to generate sphere coordinates
def create_sphere(r, center=(0,0,0), res=50):
    u, v = np.mgrid[0:2*np.pi:res*2j, 0:np.pi:res*1j]
    x = r * np.cos(u) * np.sin(v) + center[0]
    y = r * np.sin(u) * np.sin(v) + center[1]
    z = r * np.cos(v) + center[2]
    return x, y, z

# Define the Earth (Scaled for visibility)
x_earth, y_earth, z_earth = create_sphere(r=5, center=(0, 0, 0))

# Define the Black Hole (With a conceptual accretion disk)
x_bh, y_bh, z_bh = create_sphere(r=0.5, center=(12, 0, 0))

# Create the figure
fig = go.Figure()

# Add Earth surface
fig.add_trace(go.Surface(x=x_earth, y=y_earth, z=z_earth, colorscale='Blues', name='Earth', showscale=False))

# Add Black Hole surface
fig.add_trace(go.Surface(x=x_bh, y=y_bh, z=z_bh, colorscale='Greys', name='Black Hole', showscale=False))

# Add an Accretion Disk around the Black Hole
r_disk = np.linspace(0.8, 3, 20)
theta_disk = np.linspace(0, 2*np.pi, 50)
R, T = np.meshgrid(r_disk, theta_disk)
fig.add_trace(go.Surface(x=R*np.cos(T)+12, y=R*np.sin(T), z=np.zeros_like(R), colorscale='YlOrRd', opacity=0.7, showscale=False))

# Layout settings for a "Space" feel
fig.update_layout(
    title='Conceptual 3D Comparison: Earth vs. Black Hole',
    scene=dict(bgcolor='black', xaxis_visible=False, yaxis_visible=False, zaxis_visible=False),
    margin=dict(l=0, r=0, b=0, t=40)
)

fig.show()
