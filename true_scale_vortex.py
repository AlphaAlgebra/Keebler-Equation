import numpy as np
import plotly.graph_objects as go

# CONSTANTS (True AU Scale)
AU = 1.496e8 
SUN_R = 0.15 # Visual scaling for the Alpha-Anchor
VIS_ENHANCE = 1200 # 1200x visibility for planetary detection

planets = {
    'Sun':     {'d': 0.0,  'r': SUN_R, 'c': 'yellow'},
    'Mercury': {'d': 0.39, 'r': 2440/AU*VIS_ENHANCE, 'c': 'gray'},
    'Venus':   {'d': 0.72, 'r': 6052/AU*VIS_ENHANCE, 'c': 'gold'},
    'Earth':   {'d': 1.0,  'r': 6371/AU*VIS_ENHANCE, 'c': 'blue'},
    'Mars':    {'d': 1.52, 'r': 3390/AU*VIS_ENHANCE, 'c': 'red'}
}

fig = go.Figure()

for name, data in planets.items():
    phi, theta = np.mgrid[0:np.pi:20j, 0:2*np.pi:20j]
    x = data['r'] * np.sin(phi) * np.cos(theta) + data['d']
    y = data['r'] * np.sin(phi) * np.sin(theta)
    z = data['r'] * np.cos(phi)
    
    fig.add_trace(go.Surface(x=x, y=y, z=z, colorscale=[[0, data['c']], [1, data['c']]], name=name, showscale=False))
    
    if data['d'] > 0:
        t = np.linspace(0, 2*np.pi, 200)
        fig.add_trace(go.Scatter3d(x=data['d']*np.cos(t), y=data['d']*np.sin(t), z=np.zeros(200), mode='lines', line=dict(color='white', width=1), opacity=0.1, showlegend=False))

fig.update_layout(title="AETHER-VORTEX: True Scale Solar Model", scene=dict(bgcolor='black'), paper_bgcolor='black', font_color='white')
fig.show()
