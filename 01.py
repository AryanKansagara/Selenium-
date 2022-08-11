from selenium import webdriver

PATH = "D:\Desktop\selenium\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.ibm.com/cloud/learn/api")
# driver.close()#closes the tab and not the browser
print(driver.title) #this shows the title of the website
driver.quit() #quits the browser
