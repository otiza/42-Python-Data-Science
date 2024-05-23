import pandas as pd


def load(path :str) -> pd.DataFrame:
    data = pd.read_csv(path)
    print("Loading dataset of dimensions {shape}".format(shape=data.shape))
    return data


if __name__ == "__main__":
    print(load('life_expectancy_years.csv'))

