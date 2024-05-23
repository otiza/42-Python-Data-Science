from load_csv import load
import matplotlib.pyplot as plt


def display_graph(file:str,mycountry: str,country: str ) -> None:
    try:
        data = load(file)
        arr = list(data.columns)
        arr.pop(0)     
        cntry_data = list(data.loc[data['country']==country].to_numpy()[0])
        cntry_data.pop(0)
        otrcntry_data = list(data.loc[data['country']==mycountry].to_numpy()[0])
        otrcntry_data.pop(0)
        
        fig= plt.figure()
        fig, ax = plt.subplots()
        fig.suptitle('populatiton projections')
        ax.plot(arr,cntry_data)
        ax.plot(arr,otrcntry_data)
        plt.xticks(['1800','1840','1880','1920','1960','2000','2040','2080'])
        ax.set_xlabel("year")
        ax.set_ylabel("life expanctancy")  
        plt.show()
    except:
        print("error happened")



if __name__ == "__main__":
    display_graph('life.csv','Morocco',"France")



