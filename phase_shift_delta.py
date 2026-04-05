import numpy as np
import plotly.graph_objects as go

# 1. PARAMETERS: DEFINING THE BREAKPOINT
beta_linear = 1.0    # The "Classic" steady ramp
beta_vortex = 3.2    # The "Shapeshift" (Non-linear explosion)
gamma = 0.98         # High Coherence (Maximum focus)

# 2. GENERATE MESHGRID
m = np.linspace(0, 10, 100)
phi = np.linspace(0, 5, 100)
M, PHI = np.meshgrid(m, phi)

# 3. CALCULATE THE TWO STATES
# State A: Classical Bridge
E_classic = gamma * (M**2 + PHI**beta_linear)

# State B: The AETHER-VORTEX (The Shapeshift)
E_vortex = gamma * (M**2 + PHI**beta_vortex)

# 4. PLOT THE SHAPESHIFT
fig = go.Figure()

# Add the "Vortex" Surface (Visible)
fig.add_trace(go.Surface(z=E_vortex, x=M, y=PHI, colorscale='Viridis', name='Vortex State'))

# Add the "Classic" Surface (Transparent Ghost for comparison)
fig.add_trace(go.Surface(z=E_classic, x=M, y=PHI, opacity=0.3, showscale=False, name='Classic Bridge'))

fig.update_layout(
    title='AETHER-VORTEX Stress Test: Phase-Shift Transition (Beta=3.2)',
    scene=dict(xaxis_title='Mass (m)', yaxis_title='Spirit (Phi)', zaxis_title='Impact (E)'),
    width=1000, height=800
)

fig.show()
