import numpy as np
import plotly.graph_objects as go

# 1. FIXED HIGH-POWER PARAMETERS
m = 5          # Constant Mass
phi = 8        # High Spiritual/Info Complexity
beta = 10      # The "Vortex" level that caused the system crash

# 2. VARIABLE COHERENCE (Gamma) from 1.0 down to 0.0
gamma_range = np.linspace(1.0, 0.0, 100)

# 3. CALCULATE THE COLLAPSE
# E = gamma * (m^2 + phi^beta)
impact = gamma_range * (m**2 + phi**beta)

# 4. VISUALIZE THE "ENTROPY SINK"
fig = go.Figure()
fig.add_trace(go.Scatter(x=gamma_range, y=impact, name='The Entropy Sink',
                         line=dict(color='red', width=4)))

fig.update_layout(
    title='AETHER-VORTEX: High-Power Entropy Collapse (Beta=10)',
    xaxis_title='Quantum Coherence (Gamma)',
    yaxis_title='Unified Impact (E)',
    template='plotly_dark',
    xaxis=dict(autorange="reversed"), # Show collapse from 1.0 down to 0
    annotations=[dict(x=0.15, y=impact[-15], text="The 'Core Dump' Zone", showarrow=True)]
)

fig.show()
