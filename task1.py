import pulp

# Initialize the model
model = pulp.LpProblem("Maximize Production", pulp.LpMaximize)

# Define variables
Lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
Fruit_Juice = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Integer')

# Objective function (Maximize total production)
model += Lemonade + Fruit_Juice, "Total Production"

# Add constraints
model += 2 * Lemonade + 1 * Fruit_Juice <= 100  # Water constraint
model += 1 * Lemonade <= 50  # Sugar constraint
model += 1 * Lemonade <= 30  # Lemon Juice constraint
model += 2 * Fruit_Juice <= 40  # Fruit Puree constraint

# Solve the model
model.solve()

# Output results
print("Produce Lemonade:", pulp.value(Lemonade))
print("Produce Fruit Juice:", pulp.value(Fruit_Juice))
