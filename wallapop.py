from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import csv
from PIL import Image
from selenium.webdriver.common.by import By
import paddle


impicitlyWaitTime = 3
sleepTime = 3
sleep = True

options = webdriver.ChromeOptions()
#options.add_argument('--headless')
#options.add_argument('--no-sandbox')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
#options.add_argument("user-data-dir=selenium")

options.add_argument("--remote-debugging-port=9222")
options.add_argument('--disable-dev-shm-usage')
#path Portatil = "C:\\Users\\marcl\\Documents\\chromedriver.exe"
driver = webdriver.Chrome(executable_path = r"C:\\Users\\marcl\\drivers\\chromedriver_win32\\chromedriver.exe", options= options)
driver.implicitly_wait(impicitlyWaitTime)
driver.get("https://es.wallapop.com/")

act = ActionChains(driver)
count_product = 0


def Render():
 for i in range(1,22):
  act.send_keys(Keys.SPACE).perform()
 for i in range(1,192):
  act.send_keys(Keys.UP).perform()

def Sleep():
  if sleep == True:
    time.sleep(sleepTime)
    
def Read_Image(webelement):
    driver.implicitly_wait(10)
    webelement.screenshot('element.png')
    img = Image.open('element.png')
    text = paddle.paddle(img)
    return text
 
def Click_Cookies():   
    
    driver.implicitly_wait(impicitlyWaitTime)
    cookies_btn = driver.find_element(By.ID, 'onetrust-accept-btn-handler')
    act.move_to_element(cookies_btn).click().perform()
    
def Iniciar_sesion():
    
    iniciar =  driver.find_element(By.CLASS_NAME, 'btn.anchor-button_AnchorButton__gJxoN.anchor-button_AnchorButton--login__GAjI_.align-items-center')
    act.move_to_element(iniciar).click().perform()
    Sleep()
    
    iniciar_link = driver.find_element(By.CLASS_NAME, 'Welcome__btn-go-login-form')
    act.move_to_element(iniciar_link).click().perform()
    Sleep()
    
    driver.implicitly_wait(impicitlyWaitTime)
    email = driver.find_element(By.XPATH, '//*[text()="Dirección de email"]')
    act.move_to_element(email).click().send_keys("marclouzanserres99@gmail.com").perform()
    Sleep()
    
    driver.implicitly_wait(impicitlyWaitTime)
    contra = driver.find_element(By.XPATH, '//*[text()="Contraseña"]')
    act.move_to_element(contra).click().send_keys("Spyke2016").perform()
    Sleep()
    
    driver.implicitly_wait(impicitlyWaitTime)
    captcha = driver.find_element(By.XPATH, '//*[@class="AccessForm__recaptcha"]')
    act.move_to_element(captcha).click().perform()
    Sleep()
    
    iniciar_btn = driver.find_element(By.XPATH, '//*button[text()="Iniciar sesión"]')
    act.move_to_element(iniciar_btn).click().perform()
    
    
def Select_Url():
    
    urls = ["https://es.wallapop.com/search"]
    for url in urls:
        driver.get(url)
    
    content = driver.find_element(By.TAG_NAME, 'body')
    content.send_keys(Keys.PAGE_DOWN)
        
def Vender():
    
    subir_producto = driver.find_element(By.CLASS_NAME, 'btn.anchor-button_AnchorButton__gJxoN.anchor-button_AnchorButton--upload__CMTDX.align-items-center')
    act.move_to_element(subir_producto).click().perform()
        
def Extract_Products():
    
    count_product = 0

    
    
    time.sleep(5)
    driver.implicitly_wait(impicitlyWaitTime)
    #mas_productos_btn = driver.find_element(By.ID, 'btn-load-more').find_element(By.TAG_NAME, 'button')
    #act.move_to_element(mas_productos_btn).click().perform()
    #Sleep()

    Render()
        
    for a in range(0, 100): 
        
        count_product = count_product + 1
        
        Render()
        
        driver.implicitly_wait(10)
        try:
            products = driver.find_element(By.TAG_NAME, 'tsl-search-layout').find_element(By.CLASS_NAME, "ItemCardList.grid-lg-4.grid-md-3.grid-sm-2.grid-xl-4.grid-xs-2.m-auto.w-100")
            product = products.find_elements(By.CLASS_NAME, 'ItemCardList__item.ng-star-inserted')[a]
        except IndexError:
            print("No se encuentran los productos")
        
        act.move_to_element(product).click().perform()
        Sleep()
        
        panel_window = driver.window_handles[0]
        
        
        
        product_window = driver.window_handles[1]
        
        driver.switch_to.window(product_window)
        
        driver.implicitly_wait(impicitlyWaitTime)
        #price = driver.find_element(By.CLASS_NAME, 'card-product-detail').find_element(By.CLASS_NAME, 'card-product-price-info').find_element(By.TAG_NAME, 'span').text
        
       

        
        Render()
        
        
        try:
         titulo = driver.find_element(By.CLASS_NAME, 'card-product-detail-top').find_element(By.TAG_NAME, 'h1').text
         print(titulo)
        except:
         titulo = ''
        
        try:
         precio = driver.find_element(By.CLASS_NAME, 'card-product-price-info').find_element(By.TAG_NAME, 'span').text
         print(precio)
        except:
         precio = ''
        
        try:
         estado = driver.find_element(By.CLASS_NAME, 'ExtraInfo__text').text
         print(estado)
        except:
         estado = ''
        
        try:
         descripcion = driver.find_element(By.CLASS_NAME, 'js__card-product-detail--description.card-product-detail-description').text
         print(f"Descripción:  \n {descripcion}")
        except:
         descripcion = ''
        
        try:
         valoraciones = driver.find_element(By.CLASS_NAME, 'card-user-detail-reviews')
         v = Read_Image(valoraciones)
         print(v)
        except:
         v  = ''
        


        
        count_product = count_product + 1
        Sleep()
        
        driver.close()
        driver.switch_to.window(panel_window)
         
     
def main():
    Click_Cookies()
    Sleep()
    Vender()
    
   
    

if __name__ == "__main__":
    main()
    
