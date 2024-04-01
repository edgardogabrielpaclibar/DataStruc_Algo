import math
import matplotlib.pyplot as plt
import numpy as np

def solve_expression(x_values, expression):
    y_values = [max(0, expression(x)) for x in x_values]
    return y_values

def write_to_file(x_values, y_values_dict):
    with open("coordinates.txt", "w") as file:
        for i, (expression_name, values) in enumerate(y_values_dict.items(), start=1):
            file.write(str(i) + ". " + expression_name + ":\n")
            file.write(", ".join(map(str, values))) 
            file.write("\n" * 11)  

def plot_expression(x_values, y_values, expression_name, color):
    plt.figure(figsize=(12, 8))
    plt.plot(x_values, y_values, label=expression_name, linewidth=2, color=color)
    
    plt.title(f"Graph of {expression_name}")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim(left=0)
    plt.ylim(bottom=0)
    plt.legend(loc='upper left')
    plt.grid(True)
    plt.show()

def plot_all_expressions(x_values, y_values_dict):
    plt.figure(figsize=(12, 8))
    
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    
    for i, (expression_name, y_values) in enumerate(y_values_dict.items()):
        color = colors[i % len(colors)]  # mag iba sila ng color
        plt.plot(x_values, y_values, label=expression_name, linewidth=2, color=color)
    
    plt.title("Graph of All Expressions")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim(left=0)
    plt.ylim(bottom=0)
    plt.legend(loc='upper left')
    plt.grid(True)
    plt.show()

# mag himo value of x
x_values = np.linspace(0,50)

# Menu for the user to pili
expressions = {
    "x^2 + 7x + 2": lambda x: x**2 + 7*x + 2,
    "3x + 2": lambda x: 3*x + 2,
    "x^2": lambda x: x**2,
    "x^3": lambda x: x**3,
    "x^5": lambda x: x**5,
    "x^3 + 2x^2 + x + 10": lambda x: x**3 + 2*x**2 + x + 10,
    "x^4 - 3x^3 + 2x^2 + 100": lambda x: x**4 - 3*x**3 + 2*x**2 + 100,
    "sin(x)": lambda x: math.sin(x),
    "cos(x)": lambda x: math.cos(x),
    "x^5 + 4x^4 + x^3 - 2x^2 + 100": lambda x: x**5 + 4*x**4 + x**3 - 2*x**2 + 100
}

while True:
    # pakita sang expressions
    print("Available Expressions:")
    for i, expression_name in enumerate(expressions.keys()):
        print(f"{i + 1}. {expression_name}")

    # Prompt user to choose an expression or solve all
    try:
        choice = int(input("\nEnter the number of each the coordinates or pwede naman tanan 69 lang: "))
        
        if choice == 69:
            y_values_dict = {}
            for expression_name, expression in expressions.items():
                y_values = solve_expression(x_values, expression)
                y_values_dict[expression_name] = y_values
            
            # tanan eh graphn nya
            plot_all_expressions(x_values, y_values_dict)
        
            # isulat nya sa cooridnates na file
            write_to_file(x_values, y_values_dict)
            
        elif 1 <= choice <= len(expressions):
            expression_name = list(expressions.keys())[choice - 1]
            expression = expressions[expression_name]
            
            # Solve and plot the chosen expression
            y_values = solve_expression(x_values, expression)
            color = ['b', 'g', 'r', 'c', 'm', 'y', 'k'][choice % 7]  # Cycle through colors
            plot_expression(x_values, y_values, expression_name, color)
            
            # Write results to file
            write_to_file(x_values, {expression_name: y_values})
            
        else:
            print("Invalid choice. Please enter a number between 0 and", len(expressions))
        
    except ValueError:
        print("Invalid input. Please enter a number.")
    
    # Ask the user if they want to continue
    continue_choice = input("\nDo you want to enter another coordinates? (yes/no): ")
    if continue_choice.lower() != "yes":
        break
