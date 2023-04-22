import matplotlib.pyplot as plt

year = [2021, 2022, 2023, 2024, 2025]
populations = [100, 1392, 2942, 1643, 2345]


plt.plot(year, populations)

plt.title('Population by Year')
plt.xlabel('Year')
plt.ylabel('Population')

plt.legend()

plt.show()