from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 5)

url = 'https://animefire.plus/'

driver.get(url)


wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "owl-stage-outer")))
el = driver.find_element(By.CLASS_NAME, 'owl-stage-outer')