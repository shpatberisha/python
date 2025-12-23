import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("avgIQpercountry.csv")

novel_prizes_by_contient=df.groupby('Continent')['Nobel Prices'].sum()

no_of_continents=novel_prizes_by_contient.count()
print(no_of_continents)

colors=['gold','lightcoral','yellow','thistle','orange','skyblue','aqumarine','burlywood']
plt.figure(figsize=(10,10))

novel_prizes_by_contient.plot(kind="pie",colors=colors,autopct="%1.1%%")

plt.title('Distributoin of Nobel Prices by Continent')
plt.axis('equal')
plt.ylabel('')

plt.tight_layout()
plt.show()