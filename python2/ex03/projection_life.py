from load_csv import load
import matplotlib.pyplot as plt

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


def projection_of_life_expectancy(path_ippgpia: str, path_ley: str, year: str):
    ""
    try:
        assert isinstance(path_ippgpia, str), "path must be str"
        assert isinstance(path_ley, str), "path must be str"
        assert isinstance(year, str), "year must be str"
    except(AssertionError) as e:
        print(f"{type(e).__name__}: load: {e}")
        return None

    ippgpia = load(path_ippgpia)
    ley = load(path_ley)
    if ippgpia is None or ley is None:
        return None

    ippgpia_in_year = list(map(convert_population, ippgpia[year]))
    years_in_ley = ley[year]

    try:
        plt.scatter(ippgpia_in_year, years_in_ley)

        plt.title(year)
        plt.xlabel("Gross domestic product")
        plt.xscale("log")
        plt.ylabel("Life Expectancy")

        plt.show()
    except(ValueError, TypeError) as e:
            print(f"{type(e).__name__}: load: {e}")
            return None

def main():
    "main of tests"
    path1: str = "../data/income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    path2: str = "../data/life_expectancy_years.csv"
    year: str = "1900"

    projection_of_life_expectancy(path1, path2, year)


if __name__ == "__main__":
    main()
