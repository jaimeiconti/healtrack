# Para que corra en github

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

def test_func():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Ejecutar sin GUI
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get("http://127.0.0.1:5000")

        driver.find_element(By.ID, "nombre").send_keys("Jaime")
        driver.find_element(By.ID, "peso").send_keys("90")
        driver.find_element(By.TAG_NAME, "button").click()

        sleep(1)

        resultado = driver.find_element(By.ID, "resultado").text
        assert "Jaime" in resultado
        assert "90" in resultado
    finally:
        driver.quit()