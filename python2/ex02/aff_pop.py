from load_csv import load
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


def convert_population(value: str):
    ""
    if value == "":
        return 0

    multiplier = 1

    if value.endswith("k"):
        multiplier = 1000
        value = value[:-1]
    elif value.endswith("M"):
        multiplier = 1000000
        value = value[:-1]
    elif value.endswith("B"):
        multiplier = 1000000000
        value = value[:-1]

    return int(float(value) * multiplier)

def format_population(value, position):
    ""
    if value >= 1_000_000_000:
        return f"{value / 1_000_000_000:.1f}B"
    elif value >= 1_000_000:
        return f"{value / 1_000_000:.1f}M"
    elif value >= 1_000:
        return f"{value / 1_000:.1f}k"
    return str(int(value))

def graph_pop(path: str, countries: list):
    ""
    try:
        assert isinstance(path, str), "path must be str"
        assert isinstance(countries, list), "countries must be str"
    except(AssertionError) as e:
        print(f"{type(e).__name__}: load: {e}")
        return None

    data = load(path)
    if data is None:
        return None

    years = data.columns[1:]
    years = years[years <= "2050"]

    data = data.set_index("country")
    try:
        for country in countries:
            country_data = data.loc[country]
            country_data = list(map(convert_population, country_data))
            country_data = country_data[:len(years)]
            plt.plot(years, country_data, label=country)
    except(KeyError) as e:
        print(f"{type(e).__name__}: load: {e}")
        return None

    try:
        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.xticks(years[::40])
        plt.ylabel("Population")

        plt.gca().yaxis.set_major_formatter(
            FuncFormatter(format_population)
        )

        plt.legend()

        plt.show()
    except(ValueError, TypeError) as e:
            print(f"{type(e).__name__}: load: {e}")
            return None

def main():
    "main of tests"
    path: str = "../data/population_total.csv"
    countries: str = ["France", "Belgium"]

    print(graph_pop(path, countries))


if __name__ == "__main__":
    main()
