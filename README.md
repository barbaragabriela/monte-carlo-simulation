# monte-carlo-simulation

Monte Carlo simulation of a SIS epidemic spreading process in complex networks. We are interested in the calculation of the fraction of infected nodes ρ, in the stationary state, as a function of the infection rate β (at least 51 values, Δβ=0.02), for several values of the recovery rate μ (e.g. 0.1, 0.5, 0.9). Try with networks of several kinds (e.g. Erdös-Rényi, scale-free, real) and different sizes (at least 500 nodes), mean degrees, exponents, etc.

### Install requirements

```
pip install -r requirements.txt
```

### Run the simulation

For running the simulation run the following command:
```
python lab3.py
```

This is going to take a while, it runs the 3 networks, 3 times each. Erdos-Renyi networks take aproximately 1 hour each. Scale Free 2 minutes and Random Networks 15.