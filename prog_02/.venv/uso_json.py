from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from time import sleep
import json


file = open("c:\\aula_selenium\\prog_02\\.venv\\dados.json")
data_file = json.load(file)

elements = {
    'url_site': 'http://demo.automationtesting.in/Register.html',
    'first_name': '//*[@id="basicBootstrapForm"]/div[1]/div[1]/input',
    'last_name': '//*[@id="basicBootstrapForm"]/div[1]/div[2]/input',
    'address': '//*[@id="basicBootstrapForm"]/div[2]/div/textarea',
    'email': '//*[@id="eid"]/input',
    'phone': '//*[@id="basicBootstrapForm"]/div[4]/div/input',
    'male': '//*[@id="basicBootstrapForm"]/div[5]/div/label[1]/input',
    'movies': '//*[@id="checkbox2"]',
    'hockey': '//*[@id="checkbox3"]',
    'languages': '//*[@id="msdd"]',
    'languages1': '//*[@id="basicBootstrapForm"]/div[7]/div/multi-select/div[2]/ul/li[29]/a', #Portuguese
    'languages2': '//*[@id="basicBootstrapForm"]/div[7]/div/multi-select/div[2]/ul/li[8]', #English
    'skills': '//*[@id="Skills"]',
    'country': '//*[@id="countries"]',
    'select_country': '//*[@id="basicBootstrapForm"]/div[10]/div/span/span[1]/span',
    'set_country': '/html/body/span/span/span[1]/input',
    'birth': '//*[@id="yearbox"]',
    'month': '//*[@id="basicBootstrapForm"]/div[11]/div[2]/select',
    'day': '//*[@id="daybox"]',
    'password': '//*[@id="firstpassword"]',
    'confirm': '//*[@id="secondpassword"]',
    'submit': '//*[@id="submitbtn"]',
    'refresh': '//*[@id="Button1"]'
}

def preenche_formulario(driver):
    for v_ficha in data_file["ficha"]:

        first_name = driver.find_element_by_xpath(elements.get("first_name"))
        first_name.send_keys(v_ficha["first_name"])
        last_name = driver.find_element_by_xpath(elements.get("last_name"))
        last_name.send_keys(v_ficha["last_name"] + v_ficha["id"])
        address = driver.find_element_by_xpath(elements.get("address"))
        address.send_keys(v_ficha["address"])
        email = driver.find_element_by_xpath(elements.get("email"))
        email.send_keys(v_ficha["email"])
        sleep(2)
        limpa = driver.find_element_by_xpath(elements.get("refresh"))
        limpa.click()
    file.close()   # <------IMPORTANTE! fechar o arquivo depois de usar
def abrir_site(driver):
    url = elements.get("url_site")
    driver.get(url)


def setup():
    option = Options()  
    driver = webdriver.Chrome(options = option)
    return driver

def main():
    driver = setup()
    abrir_site(driver)
    preenche_formulario(driver)
    breakpoint()
    driver.quit()


if __name__ == "__main__":
    main()