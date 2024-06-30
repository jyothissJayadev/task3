import pandas as pd
import matplotlib.pyplot as plt

# Sample DataFrame
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Sales': [150, 200, 300, 250, 400, 450, 500, 550, 600, 650, 700, 750],
    'Profit': [20, 30, 50, 40, 60, 70, 80, 90, 100, 110, 120, 130]
}
df = pd.DataFrame(data)

# Bar Chart
plt.figure(figsize=(10, 5))
plt.bar(df['Month'], df['Sales'], color='blue', alpha=0.7, label='Sales')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Monthly Sales')
plt.legend()
plt.show()

# Line Chart
plt.figure(figsize=(10, 5))
plt.plot(df['Month'], df['Profit'], marker='o', color='red', label='Profit')
plt.xlabel('Month')
plt.ylabel('Profit')
plt.title('Monthly Profit')
plt.legend()
plt.show()
