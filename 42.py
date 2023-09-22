# Задача 42: Узнать какая максимальная households в зоне минимального значения population.

min_population = df.population.min()
df[
    df['population'] == min_population
].households.max()