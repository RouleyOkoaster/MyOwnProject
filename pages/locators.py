from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_USERNAME = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    BUTTON_LOGIN_SUBMIT = (By.CSS_SELECTOR, "[name = 'login_submit']")
    REG_EMAIL = (By.CSS_SELECTOR, ".form-control#id_registration-email")
    REG_PASS = (By.CSS_SELECTOR, ".form-control#id_registration-password1")
    REG_REPEAT_PASS = (By.CSS_SELECTOR, ".form-control#id_registration-password2")
    BUTTON_REG_SUBMIT = (By.CSS_SELECTOR, "[name='registration_submit']")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")