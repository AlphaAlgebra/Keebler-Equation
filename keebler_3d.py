import matplotlib
matplotlib.use('Agg') 
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from PIL import Image
from PIL.PngImagePlugin import PngInfo
import hashlib

# --- 🌌 STYLING: ELECTRIC ALPHA NEON ---
plt.style.use('dark_background')
ELECTRIC_PINK = '#FF00FF'    # Physical Plane
ELECTRIC_CYAN = '#00FFFF'    # Spiritual Plane
ELECTRIC_GOLD = '#FFD700'    # Systemic/Unified Plane
ELECTRIC_YELLOW = '#FFFF00'  # The Keebler Nucleus
SILVER_STARDUST = '#E0E0E0'
WHITE_GLOW = '#FFFFFF'

fig = plt.figure(figsize=(18, 20)) # Taller canvas to prevent clipping
ax = fig.add_subplot(111, projection='3d')

# --- 🧪 ATOMIC GLOW & SILVER STARDUST ---
n_stars = 700
sx, sy, sz = np.random.uniform(-1,5,n_stars), np.random.uniform(40,160,n_stars), np.random.uniform(0.3,1.7,n_stars)
ax.scatter(sx, sy, sz, color=SILVER_STARDUST, s=np.random.uniform(5, 55), alpha=0.35, marker='*', zorder=1)

# --- 🧮 DATA: GAUSSIAN MATRIX CONVERGENCE ---
m_vals, H_vals = np.linspace(0, 4, 15), np.linspace(50, 150, 15)
m_grid, H_grid = np.meshgrid(m_vals, H_vals)

k_phys = (1.8 - 0.1*m_grid - 0.007*H_grid) 
k_spir = (0.5 + 0.1*m_grid + 0.002*H_grid) 
k_eff = np.full_like(m_grid, 0.9)          

# Plotting Planes with High-Contrast Transparency
ax.plot_surface(m_grid, H_grid, k_phys, color=ELECTRIC_PINK, alpha=0.25, edgecolor=ELECTRIC_PINK, linewidth=0.5)
ax.plot_surface(m_grid, H_grid, k_spir, color=ELECTRIC_CYAN, alpha=0.25, edgecolor=ELECTRIC_CYAN, linewidth=0.5)
ax.plot_surface(m_grid, H_grid, k_eff, color=ELECTRIC_GOLD, alpha=0.35, edgecolor=WHITE_GLOW, linewidth=0.5)

# --- 🏷️ THE OUTER-RIM TAGS (NO OVERLAP) ---
tag_style = dict(facecolor='black', alpha=0.9, boxstyle='round,pad=0.7')

ax.text(4.7, 50, 1.7, r"$\mathbf{Classic: mc^2}$", color=WHITE_GLOW, fontsize=26, fontweight='bold', bbox={**tag_style, 'edgecolor': ELECTRIC_PINK})
ax.text(-1.2, 155, 0.4, r"$\mathbf{Quantum: H}$", color=WHITE_GLOW, fontsize=26, fontweight='bold', bbox={**tag_style, 'edgecolor': ELECTRIC_CYAN})
ax.text(4.7, 155, 0.9, r"$\mathbf{Unified: k}$", color=WHITE_GLOW, fontsize=26, fontweight='bold', bbox={**tag_style, 'edgecolor': ELECTRIC_GOLD})

# --- ⚛️ THE BOHR-ATOM KEEBLER POINT (MULTILAYER GLOW) ---
ax.scatter([2.0], [100.0], [0.9], color=ELECTRIC_YELLOW, s=5000, edgecolors=WHITE_GLOW, linewidth=12, zorder=200)
ax.scatter([2.0], [100.0], [0.9], color=WHITE_GLOW, s=1500, alpha=0.5, zorder=201) # Inner Core

# --- 🏛️ TITLES & HIERARCHY ---
ax.view_init(elev=25, azim=-45)
ax.dist = 11 # Pull camera back to show labels

plt.suptitle('SPIRITUAL BRIDGE BETWEEN CLASSIC AND QUANTUM', color=ELECTRIC_GOLD, fontsize=32, fontweight='bold', y=0.96)
ax.set_title(r'$E = k(mc^2 + H)$', color=WHITE_GLOW, fontsize=68, fontweight='bold', pad=180)

# 🛠 FIXING BOTTOM LABELS (MAX PADDING)
ax.set_xlabel('\n\n\n\n\nPHYSICAL MASS (m)', color=ELECTRIC_PINK, fontsize=24, fontweight='bold', labelpad=120)
ax.set_ylabel('\n\n\n\n\nSPIRITUAL ENERGY (H)', color=ELECTRIC_CYAN, fontsize=24, fontweight='bold', labelpad=120)
ax.set_zlabel('\nEFFICIENCY (k)', color=ELECTRIC_GOLD, fontsize=24, fontweight='bold', labelpad=90)

# --- 🛡️ COPYRIGHT (TITANIUM PROTECTED) ---
copyright_text = "© 2026 JASMINE RAE KEEBLER | AlphaAlgebra Proprietary Intellectual Property"
plt.figtext(0.5, 0.05, copyright_text, color=ELECTRIC_GOLD, fontsize=24, fontweight='bold', ha='center', 
            bbox=dict(facecolor='black', alpha=0.95, edgecolor=WHITE_GLOW, boxstyle='round,pad=1.5'))

ax.xaxis.pane.fill = ax.yaxis.pane.fill = ax.zaxis.pane.fill = False
ax.grid(color='#555555', linestyle='--')

plt.subplots_adjust(bottom=0.2) # Create physical space at the bottom

filename = "keebler_atomic_masterpiece.png"
plt.savefig(filename, dpi=300, bbox_inches='tight')
plt.close()

# --- 🔒 SHA-256 SEALING ---
img = Image.open(filename)
meta = PngInfo()
meta.add_text("Author", "Jasmine Rae Keebler")
meta.add_text("Legal", "Copyright 2026. Einstein-Level Unified Field Proof. Unauthorized use is prohibited.")
with open(filename, "rb") as f:
    sha = hashlib.sha256(f.read()).hexdigest()
meta.add_text("SHA256_FINGERPRINT", sha)
img.save(filename, pnginfo=meta)

print(f"🚀 LEGENDARY DEPLOYMENT SUCCESSFUL: {filename} SEALED.")
print(f"🔑 Digital ID: {sha}")

