import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv("titanic.csv")

# Clean age data
age_data = data['Age'].dropna()

# Gender counts
gender_count = data['Sex'].value_counts()

# Statistics
total_passengers = len(data)
male_count = gender_count['male']
female_count = gender_count['female']
average_age = round(age_data.mean(), 2)

# Dark theme
plt.style.use("dark_background")
sns.set_style("dark")

# Create dashboard
fig = plt.figure(figsize=(16,9))
gs = fig.add_gridspec(3, 4)

# Background
fig.patch.set_facecolor("#0A0A0A")

# ------------------------------------------------
# HISTOGRAM
# ------------------------------------------------
ax1 = fig.add_subplot(gs[0:2, 0:2])

sns.histplot(
    age_data,
    bins=12,
    color="#D4AF37",  # Golden Yellow
    edgecolor="white",
    ax=ax1
)

ax1.set_facecolor("#111111")

ax1.set_title(
    "📊  Age Distribution of Titanic Passengers",
    fontsize=18,
    fontweight='bold',
    color='white',
    pad=15
)

ax1.set_xlabel("Age", fontsize=13, color='white')
ax1.set_ylabel("Count", fontsize=13, color='white')

ax1.set_xticks(range(0, 81, 10))
ax1.set_yticks(range(0, 101, 20))

ax1.tick_params(colors='white')

ax1.grid(alpha=0.3)

# ------------------------------------------------
# PIE CHART
# ------------------------------------------------
ax2 = fig.add_subplot(gs[0:2, 2:4])

colors = ["#42A5F5", "#EC407A"]

ax2.pie(
    gender_count.values,
    labels=["Male", "Female"],
    autopct='%1.1f%%',
    colors=colors,
    startangle=90,
    textprops={
        'fontsize': 14,
        'color': 'white',
        'fontweight': 'bold'
    }
)

ax2.set_facecolor("#111111")

ax2.set_title(
    "👥  Gender Distribution",
    fontsize=18,
    fontweight='bold',
    color='white',
    pad=15
)

# ------------------------------------------------
# INFO BOXES
# ------------------------------------------------

gold = "#FFD700"

# Total Passengers
ax3 = fig.add_subplot(gs[2,0])
ax3.set_facecolor("#111111")
ax3.axis('off')

ax3.text(
    0.5,0.75,
    "👨‍👩‍👧‍👦",
    ha='center',
    fontsize=35
)

ax3.text(
    0.5,0.55,
    "Total Passengers",
    ha='center',
    fontsize=15,
    color='white',
    fontweight='bold'
)

ax3.text(
    0.5,0.20,
    f"{total_passengers}",
    ha='center',
    fontsize=28,
    color=gold,
    fontweight='bold'
)

# Male Passengers
ax4 = fig.add_subplot(gs[2,1])
ax4.set_facecolor("#111111")
ax4.axis('off')

ax4.text(
    0.5,0.75,
    "👨",
    ha='center',
    fontsize=35
)

ax4.text(
    0.5,0.55,
    "Male Passengers",
    ha='center',
    fontsize=15,
    color='white',
    fontweight='bold'
)

ax4.text(
    0.5,0.20,
    f"{male_count}",
    ha='center',
    fontsize=28,
    color=gold,
    fontweight='bold'
)

# Female Passengers
ax5 = fig.add_subplot(gs[2,2])
ax5.set_facecolor("#111111")
ax5.axis('off')

ax5.text(
    0.5,0.75,
    "👩",
    ha='center',
    fontsize=35
)

ax5.text(
    0.5,0.55,
    "Female Passengers",
    ha='center',
    fontsize=15,
    color='white',
    fontweight='bold'
)

ax5.text(
    0.5,0.20,
    f"{female_count}",
    ha='center',
    fontsize=28,
    color=gold,
    fontweight='bold'
)

# Average Age
ax6 = fig.add_subplot(gs[2,3])
ax6.set_facecolor("#111111")
ax6.axis('off')

ax6.text(
    0.5,0.75,
    "📅",
    ha='center',
    fontsize=35
)

ax6.text(
    0.5,0.55,
    "Average Age",
    ha='center',
    fontsize=15,
    color='white',
    fontweight='bold'
)

ax6.text(
    0.5,0.20,
    f"{average_age}",
    ha='center',
    fontsize=28,
    color=gold,
    fontweight='bold'
)

# ------------------------------------------------
# MAIN TITLE
# ------------------------------------------------

fig.suptitle(
    "✦ Titanic Passenger Data Analysis ✦",
    fontsize=30,
    fontweight='bold',
    color="#FFD700"
)

# Footer
plt.figtext(
    0.99,
    0.01,
    "Visualization using Python | Pandas | Matplotlib | Seaborn",
    horizontalalignment='right',
    fontsize=10,
    color='gray'
)

# Layout
plt.tight_layout()

# Save image
plt.savefig("titanic_dashboard.png", dpi=300)

# Show dashboard
plt.show()