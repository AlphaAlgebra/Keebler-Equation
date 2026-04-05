import plotly.graph_objects as go
import numpy as np

# 1. Setup the Mesh
range_vals = np.linspace(0, 5, 40)
M, HY = np.meshgrid(range_vals, range_vals)

# 2. Math for the Bridge
k_classic, k_quantum = 0.9, 0.6
Z_perfect = k_classic * (M + HY)
Z_actual = k_quantum * (M + HY)
Z_entropy = Z_perfect - Z_actual

fig = go.Figure()

# --- THE CLASSIC CEILING (Green) ---
fig.add_trace(go.Surface(
    x=M, y=HY, z=Z_perfect,
    colorscale=[[0, '#39FF14'], [1, '#39FF14']],
    opacity=0.2, showscale=False, name="Classic Potential"
))

# --- THE QUANTUM REALITY (Red with Floor Projection) ---
fig.add_trace(go.Surface(
    x=M, y=HY, z=Z_actual,
    surfacecolor=Z_entropy, 
    colorscale='Inferno',
    opacity=0.6,
    name="Quantum Reality",
    # THIS PART FIXES THE ERROR:
    contours=dict(
        z=dict(
            show=True,
            usecolormap=True,
            highlightcolor="yellow",
            project=dict(z=True)
        )
    )
))

# --- THE GOLD PILLAR (The Drop) ---
fig.add_trace(go.Scatter3d(
    x=[4.5, 4.5], y=[4.5, 4.5], z=[5.4, 8.1],
    mode='lines+markers',
    line=dict(color='#FFD700', width=12),
    marker=dict(size=6, color=['#FF003C', '#39FF14']),
    name="The Break"
))

# --- TITLES & BRANDING ---
fig.update_layout(
    template="plotly_dark",
    title_text="<b>CLASSIC TO QUANTUM BRIDGE</b><br><b>E = k(mc^2 + H)</b>",
    title_x=0.5,
    scene=dict(
        xaxis_title='Mass (m)',
        yaxis_title='Spiritual Energy (H)',
        zaxis_title='Total Impact (E)',
        zaxis=dict(range=[0, 10]),
        bgcolor='#000000'
    )
)

# --- JASMINE KEEBLER COPYRIGHT ---
fig.add_annotation(
    text="© JASMINE KEEBLER - ALL RIGHTS RESERVED",
    showarrow=False, xref="paper", yref="paper",
    x=0.98, y=0.02, font=dict(size=12, color="gray")
)

# 3. SAVE AS THE WEBPAGE
fig.write_html("Gold_Masterpiece.html")
print("--------------------------------------------------")
print("🚀 SUCCESS: Gold_Masterpiece.html has been created!")
print("--------------------------------------------------")
