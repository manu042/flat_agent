from selenium import webdriver


login_url = "https://sso.immobilienscout24.de/sso/login?appName=is24main&source=meinkontodropdown-login&sso_return=https://www.immobilienscout24.de/sso/login.go?source%3Dmeinkontodropdown-login%26returnUrl%3D/geschlossenerbereich/start.html?source%253Dmeinkontodropdown-login"
url = "https://www.immobilienscout24.de/expose/110546214/"
browser = webdriver.Chrome()
r = browser.get(login_url)



username = browser.find_element_by_id("username")
username.send_keys("user@example.com")

submit = browser.find_element_by_id("submit")
submit.click()

password = browser.find_element_by_id("password")
password.send_keys("password123")

login_button = browser.find_element_by_id("loginOrRegistration")
login_button.click()

r = browser.get(url)


submit = browser.find_element_by_css_selector("a[class='button-primary one-whole']")
submit.click()

textarea = browser.find_element_by_id("contactForm-Message")
textarea.send_keys("Hallo")
