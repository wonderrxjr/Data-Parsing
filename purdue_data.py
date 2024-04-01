import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('purdue.csv')
print(data.head())
print(data[0:5])

# Replace the nan values in Loc with "H"
data['Loc'] = data['Loc'].fillna('H')
print(data.head())

average_purdue_fouls = data['PF'].mean()
average_opponent_fouls = data['OPF'].mean()

total_purdue_fouls = data['PF'].sum()
total_opponent_fouls = data['OPF'].sum()

average_purdue_ft_attempts = data['FTA'].mean()
average_opponent_ft_attempts = data['OFTA'].mean()

total_purdue_ft_attempts = data['FTA'].sum()
total_opponent_ft_attempts = data['OFTA'].sum()

# Create a 2x2 grid of plots
fig, axs = plt.subplots(2, 2, figsize=(10, 10))

# Plot average Purdue fouls vs. average opponent fouls
axs[0, 0].bar(['Purdue', 'Opponent'], [average_purdue_fouls, average_opponent_fouls])
axs[0, 0].set_title('Average Fouls per Game')

# Plot total Purdue fouls vs. total opponent fouls
axs[0, 1].bar(['Purdue', 'Opponent'], [total_purdue_fouls, total_opponent_fouls])
axs[0, 1].set_title('Total Fouls')

# Plot average Purdue free throw attempts vs. average opponent free throw attempts
axs[1, 0].bar(['Purdue', 'Opponent'], [average_purdue_ft_attempts, average_opponent_ft_attempts])
axs[1, 0].set_title('Average Free Throw Attempts per Game')

# Plot total Purdue free throw attempts vs. total opponent free throw attempts
axs[1, 1].bar(['Purdue', 'Opponent'], [total_purdue_ft_attempts, total_opponent_ft_attempts])
axs[1, 1].set_title('Total Free Throw Attempts')

plt.tight_layout()
plt.show()

indiana_data = pd.read_csv('indiana.csv')

# Replace the nan values in Loc with "H"
indiana_data['Loc'] = indiana_data['Loc'].fillna('H')

average_indiana_fouls = indiana_data['PF'].mean()

total_indiana_fouls = indiana_data['PF'].sum()

average_indiana_ft_attempts = indiana_data['FTA'].mean()

total_indiana_ft_attempts = indiana_data['FTA'].sum()

# Create a 2x2 grid of plots
fig, axs = plt.subplots(2, 2, figsize=(10, 10))
# Plot average Purdue fouls vs. average Indiana fouls. Set the Purdue bar to #CEB888 and the Indiana bar to #990000
axs[0, 0].bar(['Purdue', 'Indiana'], [average_purdue_fouls, average_indiana_fouls], color=['#CEB888', '#990000'])
axs[0, 0].set_title('Average Fouls per Game')

# Plot total Purdue fouls vs. total Indiana fouls
axs[0, 1].bar(['Purdue', 'Indiana'], [total_purdue_fouls, total_indiana_fouls], color=['#CEB888', '#990000'])
axs[0, 1].set_title('Total Fouls')

# Plot average Purdue free throw attempts vs. average Indiana free throw attempts
axs[1, 0].bar(['Purdue', 'Indiana'], [average_purdue_ft_attempts, average_indiana_ft_attempts], color=['#CEB888', '#990000'])
axs[1, 0].set_title('Average Free Throw Attempts per Game')

# Plot total Purdue free throw attempts vs. total Indiana free throw attempts
axs[1, 1].bar(['Purdue', 'Indiana'], [total_purdue_ft_attempts, total_indiana_ft_attempts], color=['#CEB888', '#990000'])
axs[1, 1].set_title('Total Free Throw Attempts')

plt.tight_layout()
plt.show()

purdue_foul_diff = data['PF'] - data['OPF']

# Create a bar plot of Purdue foul differential
plt.bar(data['Date'], purdue_foul_diff)
plt.ylabel('Foul Differential')
plt.title('Purdue Foul Differential')
plt.xticks([])
plt.tight_layout()
plt.show()

# Create a scatter plot of Purdue free throw attempts vs. Purdue points. Mark the wins with a green dot and the losses with a red dot
colors = []
for i in range(len(data)):
    if 'W' in str(data['W/L'][i]):
        colors.append('green')
    else:
        colors.append('red')
plt.scatter(data['FTA'], data['Tm'], c=colors)
plt.xlabel('Free Throw Attempts')
plt.ylabel('Points')
plt.title('Purdue Free Throw Attempts vs. Points')
plt.tight_layout()
plt.show()