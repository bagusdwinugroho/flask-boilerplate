from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Setup Chrome options (headless)
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Ganti URL sesuai dengan public URL Codespaces kamu
URL = "http://localhost:5000"

driver = webdriver.Chrome(options=options)

try:
    # LOGIN
    driver.get(f"{URL}/login")
    time.sleep(1)
    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.NAME, "submit").click()

    # CREATE ITEM
    driver.get(f"{URL}/create")  # ganti dengan rute create sebenarnya
    driver.find_element(By.NAME, "nama").send_keys("Push-up 10x")
    driver.find_element(By.NAME, "submit").click()
    
    # LOGOUT
    driver.get(f"{URL}/logout")

    print("✅ Semua pengujian berhasil")

except Exception as e:
    print("❌ Gagal:", e)

finally:
    driver.quit()
