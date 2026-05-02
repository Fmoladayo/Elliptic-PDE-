"""
Experiment 3: Non-Symmetric Convection-Diffusion Equation
==========================================================
Solves -u''(x) + beta*u'(x) = f(x) on (0,1), u(0) = u(1) = 0
Exact solution: u(x) = sin(pi*x)
beta = 5, quasi-optimality constant M/alpha = 3.5

Reproduces Table 2 of the paper:
Convection-diffusion experiment with PINN baseline comparison
Widths n in {8, 16, 32, 64, 128}

Reference: Section 6.7
"""

import numpy as np

# ─── Placeholder ─────────────────────────────────────────────────
def main():
    raise NotImplementedError(
        "Full implementation will be released upon acceptance. "
        "See Section 6.7 of the paper for complete details."
    )

if __name__ == "__main__":
    main()
