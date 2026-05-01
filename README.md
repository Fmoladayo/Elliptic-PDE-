# Neural Network Approximation of Elliptic PDEs via Residual Minimisation

**Authors:** Oladayo O. Olaogun · Yohanna S. Awari  
**Affiliation:** Department of Mathematics and Statistics, Taraba State University, Jalingo, Nigeria  
**Corresponding author:** fmoladayo@gmail.com | ORCID: [0009-0000-9220-792X](https://orcid.org/0009-0000-9220-792X)  
**Journal:** Submitted to *Journal of Scientific Computing* (Springer)  
**Status:** Under review

---

## Abstract

This repository contains the code accompanying the paper:

> *Neural Network Approximation of Elliptic PDEs via Residual Minimisation: Convergence, A Posteriori Bounds, and Error Decomposition*

We develop a rigorous error analysis for approximating second-order elliptic PDEs using ReLU feedforward neural networks via dual-norm residual minimisation. The central contribution is a **three-term error decomposition** (Theorem 4.11) separating approximation, optimisation, and quadrature error with fully explicit constants, together with a **joint parameter prescription** (Corollary 4.12) that guarantees a target accuracy η simultaneously across all three design parameters.

---

## Repository Structure

```
Elliptic-PDE-/
│
├── experiments/
│   ├── experiment_1D.py          # 1D Poisson problem (Section 6.1–6.5)
│   ├── experiment_2D.py          # 2D Poisson problem (Section 6.6)
│   ├── experiment_convdiff.py    # Convection-diffusion, β = 5 (Section 6.7)
│   ├── experiment_nonsmooth.py   # Non-smooth forcing function (Section 6.8)
│   ├── experiment_A.py           # Verification of optimisation error term (Section 6.9)
│   ├── experiment_B.py           # Verification of quadrature error term (Section 6.10)
│   └── experiment_C.py           # Joint balancing prescription (Section 6.11)
│
├── models/
│   └── relu_network.py           # ReLU network class with boundary enforcement
│
├── utils/
│   └── error_utils.py            # H¹₀ error computation and residual utilities
│
├── requirements.txt              # Python dependencies
└── README.md
```

> **Note:** Code will be uploaded upon acceptance of the manuscript.

---

## Requirements

```
Python >= 3.9
torch >= 2.0
numpy
scipy
matplotlib
```

Install dependencies with:

```bash
pip install -r requirements.txt
```

---

## Reproducing the Results

All experiments use the exact solutions:
- **1D:** u(x) = sin(πx) on (0, 1)
- **2D:** u(x₁, x₂) = sin(πx₁)sin(πx₂) on (0, 1)²

Network architecture: single-hidden-layer ReLU networks with boundary enforcement  
u_θ(x) = x(1 − x)Φ_θ(x)

Training: Adam optimiser, learning rate 10⁻³, 20,000 iterations, Nq = 10,000 quadrature points.

To reproduce Table 1 (convergence over widths n ∈ {4, 8, 16, 32, 64, 128}):

```bash
python experiments/experiment_1D.py
```

---

## Key Theoretical Results

| Result | Description |
|---|---|
| Theorem 4.1 | Quasi-optimal convergence: ‖u − uₙ‖ ≤ (M/α) inf_{v ∈ Nₙ} ‖u − v‖ |
| Theorem 4.11 | Three-term error decomposition with explicit constants |
| Corollary 4.12 | Joint parameter prescription for target accuracy η |
| Proposition 4.7 | κ = O(n^{1/2}) under weight-decay regularisation Λ = O(n^{-1/2}) |

---

## Citation

If you use this code or build on this work, please cite:

```bibtex
@article{olaogun2025nn,
  title   = {Neural Network Approximation of Elliptic {PDEs} via Residual Minimisation:
             Convergence, A Posteriori Bounds, and Error Decomposition},
  author  = {Olaogun, Oladayo O. and Awari, Yohanna S.},
  journal = {Journal of Scientific Computing},
  year    = {2025},
  note    = {Under review}
}
```

---

## License

This repository is released for academic use. Full license details will be added upon publication.
