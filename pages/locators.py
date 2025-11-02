class ManagerPage:
    BUTTON_ADD_CUSTOMER = ('xpath', '//button[@ng-click="addCust()"]')
    BUTTON_CUSTOMERS = ('xpath', '//button[@ng-click="showCust()"]')
    BUTTON_ADD_CUSTOMER_FIELD = ('xpath', '//button[@type="submit" and text()="Add Customer"]')
    BUTTON_DELETE_CUSTOMER = ('xpath', '//button[@ng-click="deleteCust(cust)"]')

    FIELD_FIRST_NAME = ('xpath', '//input[@ng-model="fName"]')
    FIELD_LAST_NAME = ('xpath', '//input[@ng-model="lName"]')
    FIELD_POST_CODE = ('xpath', '//input[@ng-model="postCd"]')

    FIELD_SEARCH_CUSTOMER = ('xpath', '//input[@ng-model="searchCustomer"]')

    HEADERS_OF_CUSTOMERS_TABLE = ('xpath', '//thead/tr/td/a')

    TABLE_HEADER_FIRST_NAME = ('xpath', '//thead/tr/td/a[contains(text(), "First Name")]')

    CUSTOMERS_INFO = ('xpath', '//tr[@class="ng-scope"]/td[@class="ng-binding"]')
