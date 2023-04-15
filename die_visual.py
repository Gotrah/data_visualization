import plotly.express as px

from die import Die

# Create a D6.
die = Die()

# Make some rolls, and store results in a list.
results = [die.roll() for _ in range(1000)]
poss_results = range(1, die.num_sides+1)
frequencies = [results.count(value) for value in poss_results]

# Visualize the results.
fig = px.bar(x=poss_results, y=frequencies)
fig.show()
