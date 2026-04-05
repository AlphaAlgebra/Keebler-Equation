import numpy as np
import plotly.graph_objects as go

# 1. PARAMETERS: MASS IS NULLIFIED (m = 0)
m_zero = 0 
phi_range = np.linspace(0, 10, 100) # Scaling Spirit/Info from 0 to 10
beta_values = [1.0, 2.0, 3.2]       # Comparing Linear vs. Vortex states
gamma = 0.98                        # Maximum Coherence

fig = go.Figure()

# 2. RUN THE COMPARATIVE TEST
for b in beta_values:
    # Calculation: E = gamma * (0 + Phi^beta)
    E = gamma * (phi_range**b)
    
    label = f'Beta={b} (Classic)' if b == 1.0 else f'Beta={b} (Vortex)'
    fig.add_trace(go.Scatter(x=phi_range, y=E, name=label, mode='lines', 
                             line=dict(width=4 if b > 2 else 2)))

# 3. VISUALIZE THE "GHOST IMPACT"
fig.update_layout(
    title='AETHER-VORTEX: Pure Idea Impact (Zero Mass State)',
    xaxis_title='Spirit / Information Complexity (Phi)',
    yaxis_title='Unified Impact (E)',
    template='plotly_dark', # Use dark mode for the "Quantum" look
    annotations=
)

fig.show()
