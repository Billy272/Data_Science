import matplotlib.pyplot as plt

year = [2021, 2022, 2023, 2024, 2025]
populations = [100, 1392, 2942, 1643, 2345]


plt.plot(year, populations)

plt.title('Population by Year')
plt.xlabel('Year')
plt.ylabel('Population')

plt.legend()

plt.show()

#Generate function that creates a default DataFrame using if statements with def being better_add_column(values, df=pandas.DataFrame()):
def better_add_column(values, df=pandas.DataFrame()):
    """

    :type values: object
    """
    if df is None:
        df = pandas.DataFrame()