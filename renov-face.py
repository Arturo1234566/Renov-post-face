from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configuración del WebDriver (ChromeDriver debe estar en tu PATH)
driver = webdriver.Chrome()

# Inicia sesión en Facebook
driver.get('https://www.facebook.com')
time.sleep(3)

# Completa el login
email = driver.find_element(By.ID, 'email')
email.send_keys('sofiagutierrez190499@gmail.com')  # Reemplaza 'your_email' con tu email
password = driver.find_element(By.ID, 'pass')
password.send_keys('Sofi1904')  # Reemplaza 'your_password' con tu contraseña
password.send_keys(Keys.RETURN)
time.sleep(5)

# Navega a la página de renovación de listados
driver.get('https://www.facebook.com/marketplace/selling/renew_listings/?is_routable_dialog=true')
time.sleep(5)

# Encuentra y haz clic en el botón "Renovar"
try:
    # Busca los botones de "Renovar"
    renovar_buttons = driver.find_elements(By.XPATH, "//span[contains(text(), 'Renovar')]")

    for button in renovar_buttons:
        button.click()
        time.sleep(2)  # Espera un poco para que la acción se procese

    print("Renovaciones completadas.")
    
    # Busca los botones de "Eliminar y volver a publicar"
    eliminar_y_publicar_buttons = driver.find_elements(By.XPATH, "//span[contains(text(), 'Eliminar y volver a publicar')]")

    for button in eliminar_y_publicar_buttons:
        button.click()
        time.sleep(2)  # Espera un poco para que la acción se procese

    print("Publicaciones eliminadas y republicadas.")

except Exception as e:
    print(f"Error durante la renovación o publicación: {e}")

# Cierra el navegador
driver.quit()
