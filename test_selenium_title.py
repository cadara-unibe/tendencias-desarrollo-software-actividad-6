from selenium import webdriver
 
 
# Configuración del navegador (en este caso, utilizaremos Chrome)
driver = webdriver.Chrome()
 
 
# URL de la página que queremos probar
url = "https://www.unibe.edu.do/"
 
 
# Navegar a la página web
driver.get(url)
 
 
# Verificar si el título de la página es el esperado
expected_title = "UNIBE - Universidad Iberoamericana"
actual_title = driver.title
 
 
if expected_title == actual_title:
    print("La prueba pasó: El título de la página es correcto.")
else:
    print(f"La prueba falló: Se esperaba '{expected_title}', pero se obtuvo '{actual_title}'.")
 
 
# Cerrar el navegador
driver.quit()