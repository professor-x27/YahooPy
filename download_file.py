from selenium import webdriver
import time


def download(ticker, period="1year"):
    t = ticker
    driver = webdriver.Chrome("/Users/xavierkelly/chromedriver80")
    url = "https://finance.yahoo.com/quote/{}/history?p={}".format(t, t)

    driver.get(url)
    time.sleep(10)

    if period == "max" or period =="5y":
        driver.find_element_by_css_selector('[data-icon=CoreArrowDown]').click()
        if period == "5y":
            driver.find_element_by_css_selector('#dropdown-menu > div > ul:nth-child(2) > li:nth-child(3) > button > span').click()
        if period == "max":
            driver.find_element_by_css_selector('[data-value=MAX]').click()
        time.sleep(2)

    # if frequency == "weekly" or frequency == "monthly":
    #     driver.find_element_by_css_selector('#Col1-1-HistoricalDataTable-Proxy > section > div.Pt\(15px\).drop-down-selector.historical > div.Bgc\(\$lv1BgColor\).Bdrs\(3px\).P\(10px\) > div.D\(ib\).Py\(6px\).Mend\(10px\).smartphone_Mend\(0px\) > span > div.O\(n\)\:f.O\(n\)\:h.P\(0\).M\(0\).Cur\(p\)\:h.D\(ib\) > span > span').click()
    #     time.sleep(2)
    #     if frequency == "weekly":
    #         driver.find_element_by_css_selector('#Col1-1-HistoricalDataTable-Proxy > section > div.Pt\(15px\).drop-down-selector.historical > div.Bgc\(\$lv1BgColor\).Bdrs\(3px\).P\(10px\) > div.D\(ib\).Py\(6px\).Mend\(10px\).smartphone_Mend\(0px\) > span > div > span > span').click()
    #     if frequency == "monthly":
    #         driver.find_element_by_css_selector('#Col1-1-HistoricalDataTable-Proxy > section > div.Pt\(15px\).drop-down-selector.historical > div.Bgc\(\$lv1BgColor\).Bdrs\(3px\).P\(10px\) > div.D\(ib\).Py\(6px\).Mend\(10px\).smartphone_Mend\(0px\) > span > div > span > span').click()

    driver.find_element_by_css_selector('#Col1-1-HistoricalDataTable-Proxy > section > div.Pt\(15px\).drop-down-selector.historical > div.Bgc\(\$lv1BgColor\).Bdrs\(3px\).P\(10px\) > button > span').click()
    time.sleep(2)

    driver.find_element_by_css_selector('#Col1-1-HistoricalDataTable-Proxy > section > div.Pt\(15px\).drop-down-selector.historical > div.C\(\$tertiaryColor\).Mt\(20px\).Mb\(15px\) > span.Fl\(end\).Pos\(r\).T\(-6px\) > a > span').click()
    time.sleep(1)
    driver.close()


