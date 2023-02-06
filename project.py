import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

# Change the display options
pd.options.display.max_columns = None
pd.options.display.max_rows = None

species_df = pd.read_csv('species_info.csv')
observations_df = pd.read_csv('observations.csv')

# print(species_df.head())
# print(observations_df.head())

# Describe data of species

# print(species_df.dtypes)

species = species_df.astype({'category': 'string',
                             'scientific_name': 'string',
                             'common_names': 'string',
                             'conservation_status': 'string'})  # Change our types of columns

# print(species_df.info())
print(species_df.describe())
print(species_df.category.value_counts())
# print(species_df.conservation_status.value_counts(normalize=True))

# Pie and bar of category
"""
sub_category = species_df.category.value_counts()

plt.figure(figsize=(10, 8))

plt.pie(species_df.category.value_counts().values, labels=species_df.category.value_counts().index, autopct='%1.1f%%')

plt.suptitle('Category of species', fontweight='bold')
plt.savefig('pie_category.png')
plt.show()
"""
# Describe data of observations

# print(observations_df.dtypes)

observations_df = observations_df.astype({'scientific_name': 'string',
                                          'park_name': 'string'})

# print(observations_df.info())
print(observations_df.describe())
# print(observations_df.observations.median())
# print(observations_df.observations.mode())
# print(observations_df.observations.mad())

# The distribution of conservation_status for animals
"""
status_counts = species_df.conservation_status.value_counts()
plt.figure(figsize=(10, 8))

plt.subplot(1, 2, 1)
sns.countplot(x='conservation_status', data=species_df)

plt.xlabel('Conservation status')
plt.ylabel('Count of status')

plt.xticks(rotation=15)

plt.subplot(1, 2, 2)
plt.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%')

plt.axis('equal')

plt.suptitle('Distribution of conservation status for animals', fontweight='bold')
plt.subplots_adjust(wspace=0.5)
plt.savefig('dis_con_status.png')
plt.show()
plt.clf()
"""
# Certain types of species more likely to be endangered

influence = pd.crosstab(species_df.category, species_df.conservation_status)
influence_prop = influence / len(species_df)

print(influence)
print(influence_prop)

influence_marginals = influence_prop.sum(axis=0)
influence_marginals_1 = influence_prop.sum(axis=1)

print(influence_marginals)
print(influence_marginals_1)

chi2, pval, dof, expected = stats.chi2_contingency(influence)
print(expected)
print(chi2)

# Species were spotted the most at each park
"""
merged_df = species_df.merge(observations_df)

grouped_df = merged_df.groupby('category')['observations'].count()
print(grouped_df)
plt.figure(figsize=(15, 8))

plt.subplot(1, 2, 1)
sns.boxplot(x='category', y='observations', data=merged_df)

plt.xlabel('Species')
plt.ylabel('Number of observations')
plt.xticks(rotation=15)

plt.subplot(1, 2, 2)
plt.pie(grouped_df, labels=grouped_df.index, autopct='%1.1f%%')

plt.suptitle('Species were spotted the most at each park', fontweight='bold')

plt.savefig('species_observ.png')
plt.show()
plt.clf()
"""

# sns.histplot(x='observations', data=observations_df)
# plt.show()
print(species_df.scientific_name.mode())
