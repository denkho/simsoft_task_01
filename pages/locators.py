class ManagerPage:
    BUTTON_ADD_CUSTOMER = ('xpath', '//button[@ng-click="addCust()"]')
    BUTTON_CUSTOMERS = ('xpath', '//button[@ng-click="showCust()"]')
    BUTTON_ADD_CUSTOMER_FIELD = ('xpath', '//button[@type="submit" and text()="Add Customer"]')

    FIELD_FIRST_NAME = ('xpath', '//input[@ng-model="fName"]')
    FIELD_LAST_NAME = ('xpath', '//input[@ng-model="lName"]')
    FIELD_POST_CODE = ('xpath', '//input[@ng-model="postCd"]')

    FIELD_SEARCH_CUSTOMER = ('xpath', '//input[@ng-model="searchCustomer"]')

    CUSTOMER_INFO = ('xpath', '//tr[@class="ng-scope"]/td[@class="ng-binding"]')
