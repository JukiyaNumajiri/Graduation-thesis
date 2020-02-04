from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import chromedriver_binary

driver = webdriver.Chrome()

stock_number = [7203]

def download_stock_csv(code_range,year_range):
    for code in code_range:
        try:
            for year in year_range:
                url = 'https://kabuoji3.com/stock/{0}/{1}/'.format(code,year)
                driver.get(url)

                try:
                    driver.find_element_by_name("csv").clickq()
                    time.sleep(3)
                    driver.find_element_by_name("csv").click()
                except NoSuchElementException:
                    print("no data")
                    pass
                time.sleep(1)

        except NoSuchElementException:
            print("no data")
        pass
    time.sleep(3)

download_stock_csv(stock_number,range(1998,2019))
