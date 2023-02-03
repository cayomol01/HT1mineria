'''
4.11. (8 puntos) ¿Cómo se correlacionan los presupuestos con los ingresos? ¿Los altos
presupuestos significan altos ingresos? Haga los gráficos que necesite, histograma,
diagrama de dispersión
4.12. (7 puntos) ¿Se asocian ciertos meses de lanzamiento con mejores ingresos?
4.13. (8 puntos) ¿En qué meses se han visto los lanzamientos con mejores
ingresos?¿cuantas películas, en promedio, se han lanzado por mes?
4.14. (7 puntos) ¿Cómo se correlacionan las calificaciones con el éxito comercial?
4.15. (5 puntos) ¿A qué género principal pertenecen las películas más largas? '''


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr


#4.10 - ¿Quiénes son los directores que hicieron las 20 películas mejor calificadas?
df = pd.read_csv("movies.csv", encoding="latin1")
df_best_reviews = df.sort_values(by="voteAvg", ascending=False).head(20)
directors = df_best_reviews["releaseDate"]
print(directors)

#4.11 - ¿Cómo se correlacionan los presupuestos con los ingresos? ¿Los altos presupuestos significan altos ingresos? Haga los gráficos que necesite, histograma, diagrama de dispersión

col1, col2 = 'budget', 'revenue'
corr = df[col1].corr(df[col2])
print ("La correlación entre ", col1, " y ", col2, "es: ", round(corr, 2))

plt.scatter(df["budget"], df["revenue"], c="blue", edgecolor="black", alpha=0.3)

# Add labels to the x- and y-axes
plt.xlabel("Budget (in millions)")
plt.ylabel("Revenue (in millions)")

# Add a title to the graph
plt.title("Budget vs Revenue")

# Add gridlines to the graph
plt.grid(True)

# Show the graph
plt.show()

# Plot the histogram
plt.hist(df['budget'], bins=20, alpha=0.5, label='Budget')
plt.hist(df['revenue'], bins=20, alpha=0.5, label='Revenue')
plt.legend()
plt.xlabel('Amount in USD')
plt.ylabel('Frequency')
plt.title('Budget and Revenue Distribution')
plt.show()


#4.12. (7 puntos) ¿Se asocian ciertos meses de lanzamiento con mejores ingresos?
df['releaseDate'] = pd.to_datetime(df['releaseDate'])
df['releaseMonth'] = df['releaseDate'].dt.month

corr, p_value = pearsonr(df['releaseMonth'], df["revenue"])

print('The Pearson\'s correlation coefficient is:', corr)
print('The p-value is:', p_value)

sns.scatterplot(x='releaseMonth', y='revenue', data=df)

plt.title("Revenue by Launch Month")
plt.xlabel("Launch Month")
plt.ylabel("Revenue (in millions)")

# Show the plot
plt.show()




#4.13. (8 puntos) ¿En qué meses se han visto los lanzamientos con mejores ingresos?¿cuantas películas, en promedio, se han lanzado por mes?
# ¿En qué meses se han visto los lanzamientos con mejores ingresos?

df['releaseMonth'] = pd.to_datetime(df['releaseDate'],format='%m').dt.strftime('%b')


print(type(df['releaseMonth']))
month_revenue_average = df.groupby('releaseMonth')['revenue'].mean().sort_values(ascending=False).head(5)
print(month_revenue_average)

