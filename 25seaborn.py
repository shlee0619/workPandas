import matplotlib.pyplot as plt
import seaborn as sns


labels = ['kim', 'lee', 'aaa', 'choi']
score = [46, 90, 60, 75]


plt.plot(labels, score)
plt.title('Test Graphic')
plt.show()


sns.barplot(x=labels, y=score)
plt.title('Test Bar Plot')
plt.show()

# Penguins dataset
penguins = sns.load_dataset('penguins')
print(penguins)
print(penguins.describe())
print()
print(penguins.info())

# Titanic dataset
print('Titanic Dataset')
titanic = sns.load_dataset('titanic')
print(titanic)
print(titanic.describe())
print()
print(titanic.info())
print(titanic.head())
print(titanic.tail(10))

# sns.countplot(x='class',data =titanic)
# sns.lineplot(x='class', y='fare', data = titanic, color = 'green')
sns.barplot(x= 'class', y='fare', data =titanic)
plt.title('titanic graph')
plt.show()
