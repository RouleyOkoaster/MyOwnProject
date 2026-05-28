from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def push_the_basket_button(self):
        self.should_be_add_to_basket_button()
        self.browser.find_element(*ProductPageLocators.BUTTON_BASKET).click()

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_BASKET), "Add to basket button isnt presented"

    def should_be_title(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_TITLE), "Product title isnt presented"

    def should_be_add_messages(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGES_AFTER_ADDING_TO_BASKET), "Add message isnt presented"

    def get_the_name_of_product(self):
        self.should_be_title()
        return self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
    
    def get_the_text_from_first_add_message(self):
        self.should_be_add_messages()
        return self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_TO_BASKET_MESSAGE).text
    
    def should_be_prooduct_title_in_add_to_basket_message(self):
        assert self.get_the_name_of_product() == self.get_the_text_from_first_add_message(), "Product title should be in first message"

    def should_not_be_success_messages(self):
        assert self.is_not_element_presented(*ProductPageLocators.SUCCESS_MESSAGES), "Success messages is presented"

    def should_be_success_message_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGES), "Success messages didnt disappear"