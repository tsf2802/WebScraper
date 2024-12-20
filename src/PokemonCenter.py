from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PokemonCenter:
    URL = "https://www.pokemoncenter.com"
    PRODUCT_SELECTOR = ".product-card"  # Update based on actual HTML

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")

    def get_product_updates(self):
        try:
            self.driver.get(self.URL)
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, self.PRODUCT_SELECTOR))
            )

            products = self.driver.find_elements(By.CSS_SELECTOR, self.PRODUCT_SELECTOR)
            product_data = [
                {"name": product.text, "url": product.get_attribute("href")}
                for product in products
            ]
            return product_data
        except Exception as e:
            return {"error": str(e)}
        finally:
            self.driver.quit()
