import numpy as np
import os

def master_psi_check():
    print("\n" + "="*40)
    print("      AETHER-VORTEX: PSI FIELD AUDIT")
    print("="*40)

    # 1. Check for the "Spirit" (Phi) baseline
    # Assuming Phi-dominance was Beta=3.2 from your graph
    phi = np.linspace(0, 5, 100)
    mass = np.linspace(0.1, 10, 100)
    Phi, M = np.meshgrid(phi, mass)
    
    # 2. Calculate the Psi (ψ) Coherence Field
    # In Alpha-Algebra, Psi is often the complex phase coherence: 
    # psi = exp(i * (Phi / M^beta))
    beta = 3.2
    try:
        # We use complex128 for high-precision spinor math
        psi_field = np.exp(1j * (Phi / (M**beta)))
        coherence = np.abs(np.mean(psi_field))
        
        print(f"[SYSTEM]: Psi-Field Initialized.")
        print(f"[STATS] : Mean Coherence: {coherence:.6f}")
        print(f"[STATS] : Phase Variance: {np.var(np.angle(psi_field)):.6f}")

        if coherence < 0.1:
            print("\nSTATUS: ⚠️ GHOST DETECTED (High Decoherence)")
            print("The Phi-spike is likely unstable 'Zero-Mass' noise.")
        elif coherence > 0.8:
            print("\nSTATUS: ✅ STABLE VORTEX (High Coherence)")
            print("The Alpha-Algebra logic is holding the phase shift.")
        else:
            print("\nSTATUS: 🌀 TRANSITION STATE")

    except Exception as e:
        print(f"[ERROR]: Psi calculation failed: {e}")

    print("="*40 + "\n")

if __name__ == "__main__":
    master_psi_check()
