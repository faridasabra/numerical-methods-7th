import pandas as pd
import math
import matplotlib.pyplot as plt

def bisection(f, a, b, tol=0.01):
    if f(a) * f(b) >= 0:
        raise ValueError("Error.")
    
    N = math.ceil(math.log2((b - a) / tol)) 
    table = []
    for i in range(N):
        c = (a + b) / 2
        table.append([i+1, round(a, 4), round(b, 4), round(c, 4), round(f(a), 4), round(f(b), 4), round(f(c), 4), abs(f(c)) < tol, i+1 == N])
        
        if abs(f(c)) < tol or i+1 == N:
            return pd.DataFrame(table, columns=['i', 'a', 'b', 'c', 'f(a)', 'f(b)', 'f(c)', '|f(c)| < tol', 'i = N']), round(c, 4)
        
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    
    return pd.DataFrame(table, columns=['i', 'a', 'b', 'c', 'f(a)', 'f(b)', 'f(c)', '|f(c)| < tol', 'i = N']), None

def secant(f, a, b, tol=0.01):
    N = math.ceil(math.log2((b - a) / tol))
    table = []
    for i in range(N):
        if abs(f(b)) < tol:
            return pd.DataFrame(table, columns=['i', 'a', 'b', 'c', 'f(a)', 'f(b)', 'f(c)', '|f(c)| < tol', 'i = N']), round(b, 4)
        
        c = b - (f(b) * (b - a)) / (f(b) - f(a))
        table.append([i+1, round(a, 4), round(b, 4), round(c, 4), round(f(a), 4), round(f(b), 4), round(f(c), 4), abs(f(c)) < tol, i+1 == N])
        a, b = b, c
    
    return pd.DataFrame(table, columns=['i', 'a', 'b', 'c', 'f(a)', 'f(b)', 'f(c)', '|f(c)| < tol', 'i = N']), None

def modified_secant(f, a, b, tol=0.01):
    if f(a) * f(b) >= 0:
        raise ValueError("Error.")
    
    N = math.ceil(math.log2((b - a) / tol)) 
    table = []
    for i in range(N):
        c = b - f(b) * ((b - a) / (f(b) - f(a)))
        table.append([i+1, round(a, 4), round(b, 4), round(c, 4), round(f(a), 4), round(f(b), 4), round(f(c), 4), abs(f(c)) < tol, i+1 == N])
        
        if abs(f(c)) < tol:
            return pd.DataFrame(table, columns=['i', 'a', 'b', 'c', 'f(a)', 'f(b)', 'f(c)', '|f(c)| < tol', 'i = N']), round(c, 4)
        
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    
    return pd.DataFrame(table, columns=['i', 'a', 'b', 'c', 'f(a)', 'f(b)', 'f(c)', '|f(c)| < tol', 'i = N']), None

def newton_raphson(f, df, a, N, tol=0.01):
    table = []
    for i in range(N):
        f_a = f(a)
        df_a = df(a)
        if df_a == 0:
            return pd.DataFrame(table, columns=['i', 'x', 'f(x)', "f'(x)", '|f(x)| < tol', 'i = N']), None
        
        b = a - f_a / df_a
        table.append([i+1, round(a, 4), round(f_a, 4), round(df_a, 4), abs(f_a) < tol, i+1 == N])
        
        if abs(f_a) < tol:
            return pd.DataFrame(table, columns=['i', 'x', 'f(x)', "f'(x)", '|f(x)| < tol', 'i = N']), round(b, 4)
        
        a = b
    
    return pd.DataFrame(table, columns=['i', 'x', 'f(x)', "f'(x)", '|f(x)| < tol', 'i = N']), None

def fixed_point(f, g, a, N, tol=0.01):
    g = lambda x: f(x) + x
    table = []
    for i in range(N):
        b = g(a)
        table.append([i+1, round(a, 4), round(f(a), 4), round(g(a), 4), abs(f(a)) < tol, i+1 == N])
        
        if abs(f(a)) < tol:
            return pd.DataFrame(table, columns=['i', 'x', 'f(x)', 'g(x)', '|f(x)| < tol', 'i = N']), round(b, 4)
        
        a = b
    
    return pd.DataFrame(table, columns=['i', 'x', 'f(x)', 'g(x)', '|f(x)| < tol', 'i = N']), round(b, 4)

def display_tables(titles, solutions, dfs):
    num_tables = len(dfs)
    fig, axes = plt.subplots(nrows=num_tables, ncols=2, figsize=(12, num_tables * 2.5), facecolor="lightblue")

    if num_tables == 1:
        axes = [axes]

    plt.subplots_adjust(hspace=1.5, wspace=1.5)

    for i, (ax_text, ax_table, df, title, solution) in enumerate(zip(axes[:, 0], axes[:, 1], dfs, titles, solutions)):
        ax_text.axis("off")
        ax_text.text(0.5, 0.6, title, fontsize=12, fontweight="bold", ha="center", color="black")
        ax_text.text(0.5, 0.4, f"Solution: {solution if solution is not None else 'No root found'}", 
                     fontsize=10, ha="center", fontweight="bold", color="darkblue")

        ax_table.axis("tight")
        ax_table.axis("off")
        table = ax_table.table(cellText=df.values, 
                               colLabels=df.columns, 
                               cellLoc="center", 
                               loc="center", 
                               cellColours=[["white"] * df.shape[1]] * df.shape[0],  
                               colColours=["lightgray"] * df.shape[1])

        table.auto_set_font_size(False)
        table.set_fontsize(9)
        table.auto_set_column_width(col=list(range(len(df.columns))))

        for key, cell in table.get_celld().items():
            cell.set_edgecolor("black")
            cell.set_linewidth(1)

    plt.tight_layout()
    plt.show()

def solution():
    f = lambda x: x**2 - 3
    df = lambda x: 2*x
    g = lambda x: (3 + x**2) / (2*x)
    
    methods = [
        ("Bisection Method", bisection(f, 1, 2)),
        ("Secant Method", secant(f, 1, 2)),
        ("Modified Secant Method", modified_secant(f, 1, 2)),
        ("Newton-Raphson Method", newton_raphson(f, df, 1, 5)),
        ("Fixed Point Method", fixed_point(f, g, 1, 5))
    ]
    
    tables, solutions, titles = zip(*[(table, sol, title) for title, (table, sol) in methods])
    display_tables(titles, solutions, tables)

if __name__ == "__main__":
    solution()