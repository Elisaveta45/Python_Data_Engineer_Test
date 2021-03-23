import pandas as pd
import matplotlib.pyplot as plt

# Find the taster with the most reviews
df = pd.read_csv("wine-reviews.csv")

tester_most_reviews = df['taster_name'].value_counts().idxmax()

print(tester_most_reviews)

# Find the province with the highest average rating of the wines
prov_highest_rating = df.groupby('province')['points'].mean().idxmax()

print(prov_highest_rating)

# Check relation between points and price
correlation = df['points'].corr(df['price'])

print("Correlation = " + str(correlation))

plt.plot(df['points'], df['price'], 'ro')
plt.ylabel('price')
plt.xlabel('points')
plt.show()