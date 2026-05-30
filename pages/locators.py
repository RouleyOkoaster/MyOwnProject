from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR,"#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUTTON_GO_TO_BASKET = (By.XPATH, "(//div[@class='page_inner'])[1]//a[@class = 'btn btn-default']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
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

class ProductPageLocators():
    BUTTON_BASKET = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_TITLE = (By.XPATH, "//div[@class = 'col-sm-6 product_main']/h1")
    #MESSAGES_AFTER_ADDING_TO_BASKET = (By.XPATH, "//div[@id='messages']/div[@class='alert alert-safe alert-noicon alert-success  fade in']")
    MESSAGES_AFTER_ADDING_TO_BASKET = (By.ID, "messages")
    SUCCESS_MESSAGES = (By.CSS_SELECTOR, ".alert-success")
    PRODUCT_ADDED_TO_BASKET_MESSAGE = (By.XPATH, "//div[@id='messages']/div[1]/div[@class='alertinner ']/strong")

class BasketPageLocators():
    BASKET_ITEMS = (By.CLASS_NAME, "basket_summary")
    BASKET_EMPTY_MESSAGE = (By.XPATH, "//div[@id = 'content_inner']/p")