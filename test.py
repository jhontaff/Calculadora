from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class test :
    def __init__(self):
        opt = Options()
        opt.add_argument("--headless")
        driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=opt)
        driver.get("http://localhost:90/")
