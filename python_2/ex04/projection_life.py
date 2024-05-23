from load_csv import load
import matplotlib.pyplot as plt

def display_pnt_graph(x_axis,y_axis):
        plt.scatter(x_axis,y_axis)
        plt.title('1900')
        plt.xlabel('Gross domestic product')
        plt.ylabel('Life Expectancy')
        plt.show()

def main():
    income = load("income.csv")["1900"]
    life = load("life.csv")["1900"]
    display_pnt_graph(income,life)



if __name__ == "__main__":
    main()