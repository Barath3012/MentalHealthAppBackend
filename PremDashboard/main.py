# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from nsepy import get_history
from datetime import date
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def main(name):

    start = date(2022, 1, 1)
    end = date(2022, 5, 31)

    nifty_50 = get_history(symbol="NIFTY 50",
                           start=start,
                           end=end,
                           index=True)

    vix = get_history(symbol="VIX",
                      start=start,
                      end=end,
                      index=True)

    nifty = nifty_50[['Close']]
    vix = vix[['Close']]

    result = pd.concat([nifty, vix], axis=1).reindex()
    result.columns = ['nifty', 'vix']
    print(result)
    scatter = sns.scatterplot(data=result, x="vix", y="nifty")
    plt.show()
    return sns

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    var = main('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
