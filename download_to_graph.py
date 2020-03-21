
from selenium import webdriver
import time
import pandas as pd
import matplotlib.pyplot as plt
import platform
import os
import getpass


def download(ticker, period="1year", ret=False):
    t = ticker
    user = getpass.getuser()
    driver = webdriver.Chrome("/Users/{}/chromedriver80".format(user))
    url = "https://finance.yahoo.com/quote/{}/history?p={}".format(t, t)

    driver.get(url)
    time.sleep(10)

    if period == "max" or period =="5y":
        driver.find_element_by_css_selector('[data-icon=CoreArrowDown]').click()
        if period == "5y":
            driver.find_element_by_css_selector('#dropdown-menu > div > ul:nth-child(2) > li:nth-child(3) > button > span').click()
        if period == "max":
            driver.find_element_by_css_selector('[data-value=MAX]').click()
        time.sleep(5)

    # if frequency == "weekly" or frequency == "monthly":
    #     driver.find_element_by_css_selector('#Col1-1-HistoricalDataTable-Proxy > section > div.Pt\(15px\).drop-down-selector.historical > div.Bgc\(\$lv1BgColor\).Bdrs\(3px\).P\(10px\) > div.D\(ib\).Py\(6px\).Mend\(10px\).smartphone_Mend\(0px\) > span > div.O\(n\)\:f.O\(n\)\:h.P\(0\).M\(0\).Cur\(p\)\:h.D\(ib\) > span > span').click()
    #     time.sleep(2)
    #     if frequency == "weekly":
    #         driver.find_element_by_css_selector('#Col1-1-HistoricalDataTable-Proxy > section > div.Pt\(15px\).drop-down-selector.historical > div.Bgc\(\$lv1BgColor\).Bdrs\(3px\).P\(10px\) > div.D\(ib\).Py\(6px\).Mend\(10px\).smartphone_Mend\(0px\) > span > div > span > span').click()
    #     if frequency == "monthly":
    #         driver.find_element_by_css_selector('#Col1-1-HistoricalDataTable-Proxy > section > div.Pt\(15px\).drop-down-selector.historical > div.Bgc\(\$lv1BgColor\).Bdrs\(3px\).P\(10px\) > div.D\(ib\).Py\(6px\).Mend\(10px\).smartphone_Mend\(0px\) > span > div > span > span').click()

    driver.find_element_by_css_selector('#Col1-1-HistoricalDataTable-Proxy > section > div.Pt\(15px\).drop-down-selector.historical > div.Bgc\(\$lv1BgColor\).Bdrs\(3px\).P\(10px\) > button > span').click()
    time.sleep(5)

    driver.find_element_by_css_selector('#Col1-1-HistoricalDataTable-Proxy > section > div.Pt\(15px\).drop-down-selector.historical > div.C\(\$tertiaryColor\).Mt\(20px\).Mb\(15px\) > span.Fl\(end\).Pos\(r\).T\(-6px\) > a > span').click()
    time.sleep(1)
    driver.close()

    if ret is True:
        output = ticker + ".csv"
        return output


def plot_yahoo_csv(file, x, y, ret=False, save=False, show=False):
    if platform.system() == "Windows":
        user = "CHOOSE"
        path = "C:\\Users\\{}\\Downloads\\{}".format(user, file)
        loc = "C:\\Users\\{}\\Desktop".format(user)
    elif platform.system() == "Darwin":
        user = getpass.getuser()
        path = "/Users/{}/Downloads/{}".format(user, file)
        loc = "/Users/{}/Desktop".format(user)
    data = pd.read_csv(path)
    data.plot(kind="line", x=x, y=y)
    plt.title(label="{} given {}".format(y, x))

    if ret is True:
        return data
    if save is True:
        n = file.index(".")
        arr_name = []
        for i in range(n):
            arr_name += file[i]
        plot_name = "".join(arr_name)
        os.chdir(loc)
        name = plot_name + ".png"
        plt.savefig(name)
    if show is True:
        plt.show()



def download_to_graph(ticker, x, y, periodm ="1year", retm=False, savem=False, retd=True, showm=False):
    file = download(ticker, ret=retd, period=periodm)
    plot_yahoo_csv(file, x, y, ret=retm, save=savem, show=showm)
    user = getpass.getuser()
    loc = "/Users/{}/Desktop/".format(user)
    os.chdir(loc)
    os.system("open " + loc + ticker + ".png")



print("Function dict:")
f_dict = {"download_to_graph": "ticker, x, y, periodm ='1year', retm=False, savem=False, retd=True, showm=False"}
print(f_dict)
print("NOTE: All Saves located in Desktop")


