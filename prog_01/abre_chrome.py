from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep


def setup():
    option = Options()  
    driver = webdriver.Chrome(options = option)
    return driver

def abrir_site(driver):
       v_url = "https://www.google.com"
       driver.get(v_url)
       driver.implicitly_wait(30)  # tempo em segundos



def formulario(driver):
    v_pesquisa = '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'
    v_campo = driver.find_element_by_xpath(v_pesquisa)
    v_campo.send_keys("blueshift brasil")
    sleep(2)
    v_campo.send_keys(Keys.ENTER)
    sleep(2)
    v_campo = driver.find_element_by_xpath('//*[@id="tsf"]/div[1]/div[1]/div[2]/div/div[2]/input')
    v_campo.click()
    v_campo.send_keys(Keys.CONTROL, 'a')
    sleep(3)
    v_campo.send_keys(Keys.CONTROL, 'c')
    sleep(3)
    v_campo.send_keys(Keys.CONTROL, 'v')


def main():
    driver = setup()
    abrir_site(driver)
    formulario(driver)
    breakpoint()
    driver.quit()


if __name__ == "__main__":
    main()

