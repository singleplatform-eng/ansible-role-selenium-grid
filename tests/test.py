from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
desired_capabilities = chrome_options.to_capabilities()
driver = webdriver.Remote(command_executor="http://localhost:4444/wd/hub", desired_capabilities=desired_capabilities)

driver.get('https://google.com/xhtml')
driver.quit()
