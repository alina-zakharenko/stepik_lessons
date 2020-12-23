from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_msg(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MSG), \
            "Text that products aren't added isn't present"

    def should_be_no_products_in_the_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_IN_BASKET_MSG), \
            "Products are presented in a basket, but should not be"
