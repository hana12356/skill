def solve_expression(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Error: {str(e)}"


user_expression = input("Enter an arithmetic expression: ")
print(f"Result: {solve_expression(user_expression)}")
