"""
Experiment 4: Non-Smooth Forcing Function
==========================================
Solves -u''(x) = f(x) on (0,1), u(0) = u(1) = 0
f(x) = 2 for x < 0.5, f(x) = -2 for x >= 0.5
Exact solution: u in H^1_0(0,1) \ H^2(0,1)

Reproduces Table 3 of the paper:
Reduced regularity experiment showing degraded convergence rate
Observed rate approx n^{-0.82}
Widths n in {8, 16, 32, 64, 128}

Reference: Section 6.8
"""

import numpy as np

# ─── Placeholder ─────────────────────────────────────────────────
def main():
    raise NotImplementedError(
        "Full implementation will be released upon acceptance. "
        "See Section 6.8 of the paper for complete details."
    )

if __name__ == "__main__":
    main()
