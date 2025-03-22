def display_tables(dfs, titles, solutions):
    num_tables = len(dfs)
    fig, axes = plt.subplots(nrows=num_tables, figsize=(8, num_tables * 2))  # Reduce figure size
    
    if num_tables == 1:
        axes = [axes]  # Ensure axes is iterable when there's only one table
    
    plt.subplots_adjust(hspace=0.5)  # Reduce space between tables

    for i, (ax, df, title, solution) in enumerate(zip(axes, dfs, titles, solutions)):
        ax.set_title(title, fontsize=14, fontweight="bold", pad=8, color="darkblue")
        ax.axis("tight")
        ax.axis("off")
        
        # Create table with a cleaner look
        table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc="center", loc="center", edges="horizontal")
        table.auto_set_font_size(False)
        table.set_fontsize(9)  # Smaller font to fit better
        table.auto_set_column_width(col=list(range(len(df.columns))))  # Ensure consistent column width
        
        # Add solution text right under the table in the same figure
        ax.text(0.5, -0.3, f"Solution: {solution if solution is not None else 'No root found'}", 
                ha="center", fontsize=10, fontweight="bold", color="darkred", transform=ax.transAxes)

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
        ("Newton-Raphson Method", newton_raphson(f, df, 1)),
        ("Fixed Point Iteration", fixed_point(g, f, 1, 5))
    ]
    
    tables, solutions, titles = zip(*[(table, sol, title) for title, (table, sol) in methods])
    display_tables(tables, titles, solutions)