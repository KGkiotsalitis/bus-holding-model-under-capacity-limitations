# An analytic solution for real-time bus holding subject to vehicle capacity limits

This repository is meant for publishing some of the code related to the **real time bus holding problem under capacity limitations** applied in public transit (in particular, **bus services**).

Currently, this repository contains a couple of modules:

1. The `singapore_scenario.aimms.py` script in the folder Singapore_scenario contains the devised bus holding model introduced in the paper **An analytic solution for real-time bus holding subject to vehicle capacity limits**, which is currently published at Transportation Research Part C: Emerging Technologies. This script contains all necessary functions to calculate the solution of the mathematical program for different parameter values and idealized/real scenarios. In the same script, the proposed analytic solution of the paper **An analytic solution for real-time bus holding subject to vehicle capacity limits** is also computed demonstrating its equivalency to the solution of the mathematical program.

2. The `comparison_with_benchmark.py` script that computes the analytic solution for different parameter values. For this, we have created 4 scenarios: `scenario I.py`, `scenario II.py`, `scenario III.py`, `scenario IV.py`.

# Referencing

In case you use this code for scientific purposes, it is appreciated if you provide a citation to the paper:

**Gkiotsalitis, K., and E. C. Van Berkum.** An analytic solution for real-time bus holding subject to vehicle capacity limits. Transportation Research Part C: Emerging Technologies 121 (2020): 102815.

# License

MIT License

# Dependencies

Note that the script `comparison_with_benchmark.py` is written in Python. Running or modifying this script requires an installed version of **Python 3.6**. 

Note that the mathematical program of the bus holding problem under capacity limitations `singapore_scenario.aimms` is written in AIMMS that uses CPLEX. Running or modifying this script requires an installed version of **AIMMS**. A free academic license in available at: https://aimms.com/english/developers/licensing/free-licenses/aimmsacademiclicense/
