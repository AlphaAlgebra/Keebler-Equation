import numpy as np
import plotly.graph_objects as go

# CONSTANTS (True AU Scale)
AU = 1.496e8 
SUN_R = 696340 / AU 
VIS_ENHANCE = 1000 # 1000x visibility so you can actually see the planets

planets = {
    'Sun':     {'d': 0.0,  'r': 696340, 'c': 'yellow'},
    'Mercury': {'d': 0.39, 'r': 2440,   'c': 'gray'},
    'Venus':   {'d': 0.72, 'r': 6052,   'c': 'gold'},
    'Earth':   {'d': 1.0,  'r': 6371,   'c': 'blue'},
    'Mars':    {'d': 1.52, 'r': 3390,   'c': 'red'}
}

fig = go.Figure()

for name, data in planets.items():
    # True Math + Visual Enhancement
    r_au = (data['r'] / AU) * VIS_ENHANCE
    phi, theta = np.mgrid[0:np.pi:20j, 0:2*np.pi:20j]
    x = r_au * np.sin(phi) * np.cos(theta) + data['d']
    y = r_au * np.sin(phi) * np.sin(theta)
    z = r_au * np.cos(phi)
    
    fig.add_trace(go.Surface(x=x, y=y, z=z, colorscale=[[0, data['c']], [1, data['c']]], name=name, showscale=False))
    
    if data['d'] > 0:
        t = np.linspace(0, 2*np.pi, 200)
        fig.add_trace(go.Scatter3d(x=data['d']*np.cos(t), y=data['d']*np.sin(t), z=np.zeros(200), mode='lines', line=dict(color='white', width=1), opacity=0.2, showlegend=False))

fig.update_layout(title="AETHER-VORTEX: True Scale Inner System", scene=dict(bgcolor='black'), margin=dict(l=0, r=0, b=0, t=40))
fig.show()
