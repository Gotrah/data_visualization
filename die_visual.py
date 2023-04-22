import plotly.express as px

from die import Die

# Create a D6.
die_1 = Die()
die_2 = Die(num_sides=6)

# Make some rolls, and store results in a list.
results = [die_1.roll() * die_2.roll() for _ in range(50_000)]
max_result = die_1.num_sides * die_2.num_sides
min_result = 1
poss_results = range(min_result, max_result+1)
frequencies = [results.count(value) for value in poss_results]

# Visualize the results.
title = "Results of rolling a D6 and a D10 50,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Results'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Further customize chart.
fig.update_layout(xaxis=dict(dtick=1))

fig.write_html('dice_visual_d6d10.html')
fig.show()

