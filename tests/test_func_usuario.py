from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5000")

# Llena los campos
driver.find_element(By.ID, "nombre").send_keys("Jaime")
driver.find_element(By.ID, "peso").send_keys("90")

# Submit
driver.find_element(By.TAG_NAME, "button").click()

sleep(1)

resultado = driver.find_element(By.ID, "resultado").text
# Validar resultado
assert "Jaime" in resultado
assert "90" in resultado
print("PRUEBA FUNCIONAL EXITOSA!!!")
driver.quit()