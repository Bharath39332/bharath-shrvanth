import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('mtcars.csv')

# Display first 10 rows
print("First 10 rows of the dataset:")
print(df.head(10))


plt.figure(figsize=(6, 4))
plt.hist(df['mpg'], bins=10, edgecolor='black')
plt.title('Histogram of MPG')
plt.xlabel('MPG')
plt.ylabel('Frequency')
plt.show()


plt.figure(figsize=(6, 4))
plt.scatter(df['wt'], df['mpg'], color='blue')
plt.title('Scatter Plot of Weight vs MPG')
plt.xlabel('Weight (wt)')
plt.ylabel('Miles per Gallon (mpg)')
plt.show()


plt.figure(figsize=(6, 4))
df['am'].value_counts().sort_index().plot(kind='bar')
plt.title('Transmission Type Counts (am)')
plt.xlabel('am (0 = automatic, 1 = manual)')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(6, 4))
sns.boxplot(x=df['mpg'])
plt.title('Boxplot of MPG')
plt.xlabel('MPG')
plt.show()

print("Minimum MPG:", df['mpg'].min())
print("Maximum MPG:", df['mpg'].max())


print("MPG Quantiles:")
print(df['mpg'].quantile([0.1, 0.25, 0.5, 0.75]))
