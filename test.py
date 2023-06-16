from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
class test():
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get("http://localhost/")
        path1 = "//div[normalize-space()='1']"  
        path2 = "//div[normalize-space()='2']"  
        path3 = "//div[normalize-space()='3']"  
        path4 = "//div[normalize-space()='4']"  
        path5 = "//div[normalize-space()='5']"  
        pathmas = "//div[normalize-space()='+']"
        pathmenos = "//div[normalize-space()='-']"
        pathpor = "//div[normalize-space()='*']"
        pathequ = "//div[normalize-space()='=']"
        pathres="//div[@class='calculator-display']"
        pathc= "//div[normalize-space()='C']"
        pathdiv ="//div[3]"
        btn1 = driver.find_element(By.XPATH,path1)
        btn2 = driver.find_element(By.XPATH,path2)
        btn3 = driver.find_element(By.XPATH,path3)
        btn4 = driver.find_element(By.XPATH,path4)
        btn5 = driver.find_element(By.XPATH,path5)
        btnmas=driver.find_element(By.XPATH,pathmas)
        btnmenos=driver.find_element(By.XPATH,pathmenos)
        btnpor=driver.find_element(By.XPATH,pathpor)
        btnequ=driver.find_element(By.XPATH,pathequ)
        btnc=driver.find_element(By.XPATH,pathc)
        btndiv=driver.find_element(By.XPATH,pathdiv)
        res = driver.find_element(By.XPATH,pathres)
        # multiplicación
        btn2.click()
        btnpor.click()
        btn5.click()
        btnequ.click()
        print(f"Resultado multiplicación {res.text}")
        assert res.text == "10"
        btnc.click()
        time.sleep(1)
        # suma
        btn4.click()
        btnmas.click()
        btn3.click()
        btnequ.click()
        print(f"Resultado suma {res.text}")
        assert res.text == "7"
        btnc.click()
        time.sleep(1)
        # resta
        btn1.click()
        btnmenos.click()
        btn4.click()
        btnequ.click()
        print(f"Resultado resta {res.text}")
        assert res.text == "-3"
        btnc.click()
        time.sleep(1)
        # división
        btn4.click()
        btndiv.click()
        btn2.click()
        btnequ.click()
        print(f"Resultado división {res.text}")
        assert res.text == "2"
        btnc.click()
        driver.quit()

test()

