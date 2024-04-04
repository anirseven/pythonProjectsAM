from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#server = 'http://localhost:4444'

options = webdriver.ChromeOptions()
#driver = webdriver.Remote(command_executor=server, options=options)
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.maximize_window()
driver.implicitly_wait(10)

# Automating form
driver.find_element(By.XPATH, "//input[@value='radio2']").click()
driver.find_element(By.ID, "autocomplete").send_keys("Ind")
countries = driver.find_elements(By.XPATH, "//li[@class='ui-menu-item']")
for country in countries:
    if country.text == "India":
        country.click()
        break

dropdown = Select(driver.find_element(By.ID, "dropdown-class-example"))
dropdown.select_by_visible_text("Option2")
driver.find_element(By.ID, "checkBoxOption3").click()

#multiple windows
driver.find_element(By.ID, "openwindow").click()
windows = driver.window_handles
driver.switch_to.window(windows[1])
print(driver.title)
driver.switch_to.window((windows[0]))
print(driver.title)

#multiple tabs
driver.find_element(By.ID, "opentab").click()
tabs = driver.window_handles
driver.switch_to.window(tabs[1])
print(driver.title)
driver.switch_to.window(tabs[0])
print(driver.title)

#alert
driver.find_element(By.ID, "confirmbtn").click()
alert = driver.switch_to.alert
print(alert.text)
alert.accept()
driver.switch_to.default_content()

#Mousehover

action = ActionChains(driver)
element = driver.find_element(By.ID, "mousehover")
action.move_to_element(element).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()

#webtable
rows = driver.find_elements(By.XPATH, "//table[@name='courses']/tbody/tr")
columns = driver.find_elements(By.XPATH, "//table[@name='courses']/tbody/tr/td[2]")
for r in rows:
    for c in columns:
        if c.text == 'WebSecurity Testing for Beginners-QA knowledge to next level':
            price = r.find_element(By.XPATH, "//table[@name='courses']/tbody/tr/td[3]").text
            print(price)
            break
    break