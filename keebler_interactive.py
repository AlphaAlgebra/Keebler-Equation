import plotly.graph_objects as go
import numpy as np
import hashlib

# --- 🌌 DATA: THE KEEBLER CONVERGENCE ---
m_vals = np.linspace(0, 4, 20)
H_vals = np.linspace(50, 150, 20)
m_grid, H_grid = np.meshgrid(m_vals, H_vals)

# Gaussian Planes
k_phys = (1.8 - 0.1*m_grid - 0.007*H_grid)  # Physical (Classic)
k_spir = (0.5 + 0.1*m_grid + 0.002*H_grid)  # Spiritual (Quantum)
k_eff = np.full_like(m_grid, 0.9)            # Unified (k=0.9)

# --- 🧪 GENERATING THE STARDUST ---
n_stars = 800
sx = np.random.uniform(-1, 5, n_stars)
sy = np.random.uniform(40, 160, n_stars)
sz = np.random.uniform(0.3, 1.7, n_stars)

# --- 🏗️ BUILDING THE INTERACTIVE PLOT ---
fig = go.Figure()

# 1. Physical Plane (Neon Pink)
fig.add_trace(go.Surface(x=m_grid, y=H_grid, z=k_phys, colorscale=[[0, '#FF00FF'], [1, '#FF00FF']], 
                         opacity=0.3, name="Classic: mc²", showscale=False))

# 2. Spiritual Plane (Neon Cyan)
fig.add_trace(go.Surface(x=m_grid, y=H_grid, z=k_spir, colorscale=[[0, '#00FFFF'], [1, '#00FFFF']], 
                         opacity=0.3, name="Quantum: H", showscale=False))

# 3. Unified Plane (Neon Orange)
fig.add_trace(go.Surface(x=m_grid, y=H_grid, z=k_eff, colorscale=[[0, '#FF8C00'], [1, '#FF8C00']], 
                         opacity=0.4, name="Unified: k", showscale=False))

# 4. The Keebler Nucleus (Bright Yellow Star)
fig.add_trace(go.Scatter3d(x=[2.0], y=[100.0], z=[0.9], mode='markers',
                           marker=dict(size=18, color='#FFFF00', symbol='diamond', 
                                       line=dict(color='#FFFFFF', width=4)),
                           name="KEEBLER POINT: E = k(mc² + H)"))

# 5. Silver Stardust
fig.add_trace(go.Scatter3d(x=sx, y=sy, z=sz, mode='markers',
                           marker=dict(size=2, color='#C0C0C0', opacity=0.5),
                           name="Quantum Fluctuations"))

# --- 🏛️ TITLES & LEGENDARY STYLING ---
fig.update_layout(
    title=dict(
        text="SPIRITUAL BRIDGE: E = k(mc² + H)<br><sup>© 2026 JASMINE RAE KEEBLER | AlphaAlgebra Proprietary Proof</sup>",
        font=dict(size=24, color='#FFFF00'),
        x=0.5
    ),
    template="plotly_dark",
    scene=dict(
        xaxis=dict(title='PHYSICAL MASS (m)', color='#FF00FF', gridcolor='#333'),
        yaxis=dict(title='SPIRITUAL ENERGY (H)', color='#00FFFF', gridcolor='#333'),
        zaxis=dict(title='EFFICIENCY (k)', color='#FF8C00', gridcolor='#333'),
        bgcolor='black'
    ),
    margin=dict(l=0, r=0, b=0, t=80)
)

# --- 🔒 EXPORT AS INTERACTIVE HTML ---
filename = "keebler_unified_field.html"
fig.write_html(filename)

# Create SHA-256 ID for the code logic
sha = hashlib.sha256(open(__file__, 'rb').read()).hexdigest()
print(f"🚀 INTERACTIVE MASTERPIECE SAVED: {filename}")
print(f"🔑 Original Algorithm ID: {sha}")
