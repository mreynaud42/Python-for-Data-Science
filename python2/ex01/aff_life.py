from load_csv import load
import matplotlib.pyplot as plt

def graph_country(path: str, country: str) -> None:
    ""
    try:
        assert isinstance(path, str), "path must be str"
        assert isinstance(country, str), "country must be str"
    except(AssertionError) as e:
        print(f"{type(e).__name__}: load: {e}")
        return None

    data = load(path)
    if data is None:
        return None

    years = data.columns[1:]

    data = data.set_index("country")
    try:
        country_data = data.loc[country]
    except(KeyError) as e:
        print(f"{type(e).__name__}: load: {e}")
        return None

    try:
        plt.plot(years, country_data)

        plt.title(f"{country} Life expectancy Projections ")
        plt.xlabel("Year")
        plt.xticks(years[::40])
        plt.ylabel("Life expectancy")

        plt.show()
    except(ValueError, TypeError) as e:
            print(f"{type(e).__name__}: load: {e}")
            return None

def main():
    "main of tests"
    path: str = "../data/life_expectancy_years.csv"
    country: str = "France"

    print(graph_country(path, country))


if __name__ == "__main__":
    main()