import matplotlib
matplotlib.use('Agg')  # safe for headless environments
import matplotlib.pyplot as plt
import numpy as np

def make_square_h():
    # Return square in homogeneous coords (N, 3), closed polygon
    S = np.array([
        [0.0, 0.0, 1.0],
        [1.0, 0.0, 1.0],
        [1.0, 1.0, 1.0],
        [0.0, 1.0, 1.0],
        [0.0, 0.0, 1.0],
    ])
    return S

def translation_matrix(dx, dy):
    T = np.array([
        [1.0, 0.0, dx],
        [0.0, 1.0, dy],
        [0.0, 0.0, 1.0],
    ])
    return T

def apply_T(S_h, T):
    # S_h: (N, 3) with row-vectors; apply S' = S * T^T for row-vector convention
    return (S_h @ T.T)

def to_xy(S_h):
    # Convert homogeneous (N,3) -> (N,2)
    return S_h[:, :2] / S_h[:, 2:3]

# --- Config ---
dx, dy = 0.6, 0.1   # per-step translation
num_steps = 5

S0_h = make_square_h()
T = translation_matrix(dx, dy)

fig = plt.figure()
Si_h = S0_h.copy()

for i in range(num_steps + 1):
    Si_xy = to_xy(Si_h)
    plt.plot(Si_xy[:, 0], Si_xy[:, 1], marker='o', label=f'Step {i}', alpha=0.9 - i*0.1)
    # Next state: S_{i+1} = T * S_i
    Si_h = apply_T(Si_h, T)

plt.axis('equal')
plt.grid(True, linestyle='--', alpha=0.4)
plt.legend()
plt.tight_layout()
plt.savefig('translation_steps_homogeneous.png', dpi=150)
print("Saved to translation_steps_homogeneous.png")

