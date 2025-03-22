# Numerical Methods for Root Finding

## Overview
This project implements several numerical methods for finding the roots of a given function. These methods include:
- Bisection Method
- Secant Method
- Modified Secant Method
- Newton-Raphson Method
- Fixed Point Iteration Method

Each method iterates through possible solutions until a specified tolerance level is reached. The results are presented in tabular form and visualized using Matplotlib and Seaborn.

## Features
- Implements multiple root-finding algorithms.
- Provides a step-by-step table of iterations for each method.
- Uses Pandas to structure output tables.
- Visualizes results using Matplotlib.

## Requirements
Ensure you have the following Python libraries installed:
```bash
pip install numpy pandas matplotlib seaborn
```

## Usage
Run the script with:
```bash
python main.py
```
The program will compute the roots using different methods and display the results.

## Function Descriptions
- **bisection(f, a, b, tol=0.01):** Implements the Bisection Method.
- **secant(f, a, b, tol=0.01):** Implements the Secant Method.
- **modified_secant(f, a, b, tol=0.01):** Implements a variation of the Secant Method.
- **newton_raphson(f, df, a, tol=0.01, max_i=50):** Implements the Newton-Raphson Method.
- **fixed_point(g, f, a, N, tol=0.01):** Implements the Fixed Point Iteration Method.
- **display_tables(titles, solutions, dfs):** Formats and displays the iteration results.
- **solution():** Runs the methods on the function f(x) = x^2 - 3 and visualizes the output.

## Example Function Used
The default function used in the script is:
```python
f = lambda x: x**2 - 3
```

## Output
The program will generate tabular results and display them using Matplotlib. Each method will show the computed root (if found) and the step-by-step calculation process.

## License
This project is licensed under the MIT License.

