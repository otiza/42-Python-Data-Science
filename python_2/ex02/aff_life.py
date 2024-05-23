from load_csv import load
import matplotlib.pyplot as plt


def display_graph(file:str,country: str ) -> None:
    try:
        data = load(file)
        arr = list(data.columns)
        arr.pop(0)     
        cntry_data = list(data.loc[data['country']==country].to_numpy()[0])
        cntry_data.pop(0)
        datas=[arr,cntry_data]
        fig= plt.figure()
        fig, ax = plt.subplots()
        fig.suptitle('{pa} life expactancy'.format(pa=country))
        ax.plot(datas[0],datas[1])
        plt.xticks(['1800','1840','1880','1920','1960','2000','2040','2080'])
        ax.set_xlabel("year")
        ax.set_ylabel("life expanctancy")  
        plt.show()
    except:
        print("error happened")



if __name__ == "__main__":
    display_graph('life.csv','Morocco')



