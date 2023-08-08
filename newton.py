def newton_method(func, derivative, initial_guess, tol=1e-6, max_iter=100):
    x = initial_guess
    iteration = 0
    
    while abs(func(x)) > tol and iteration < max_iter:
        x = x - func(x) / derivative(x)
        iteration += 1
    
    return x

# Get user input for the function as a string
func_str = input("Enter the function in terms of 'x': ")

# Create a function object from the user-provided function string
def user_function(x):
    return eval(func_str)

# Get user input for the derivative as a string
derivative_str = input("Enter the derivative of the function in terms of 'x': ")

# Create a function object from the user-provided derivative string
def user_derivative(x):
    return eval(derivative_str)

# Get user input for the initial guess
initial_guess = float(input("Enter the initial guess for the root: "))

root = newton_method(user_function, user_derivative, initial_guess)

print(f"Root found at x = {root:.6f}")
