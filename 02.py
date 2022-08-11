from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "D:\Desktop\selenium\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://techwithtim.net")

print(driver.title)
search = driver.find_element(value="s")#finding the element with the value "s"
search.send_keys("test")#types this in search bar
search.send_keys(Keys.RETURN)#pressing enter to get search results

# print(driver.page_source)

#the below code is used to wait before we find the id or before we move to the next part of the script 
#also this will print all the text of the tag with the id main 
#this is called EXPLICIT WAITS more in documentation
# try:
#     main = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "main"))
#     )
#     print(main.text)
# except:
#     driver.quit()


try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    articles = main.find_elements(By.TAG_NAME,"article")
    for article in articles:
        header = article.find_element(By.CLASS_NAME,"entry-summary")
        print(header.text)
finally:
    driver.quit()



# main = driver.find_element(by="main") 
# print(main.text)

# time.sleep(5)#timeout of 5 seconds
# driver.quit() 
