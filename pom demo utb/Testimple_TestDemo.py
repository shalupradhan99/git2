from selenium import webdriver
from Regi_TestDemo import RegisterAccountPage, AddressBookPage  # Correct import statement
import time
def test_register_account():
    driver = webdriver.Chrome()
    driver.get("https://demo.opencart.com.gr/")
    driver.maximize_window()
    time.sleep(5)
    # Step 1: Login
    register_account_page = RegisterAccountPage(driver)
    register_account_page.verify_main_page_header()
    register_account_page.go_to_register_account_page()
    register_account_page.verify_warning_message()
    register_account_page.enter_first_name("Shalu")
    register_account_page.verify_first_name_error()
    register_account_page.clear_and_enter_first_name("Shalu")
    register_account_page.enter_last_name("pradhan")
    register_account_page.verify_last_name_error()
    register_account_page.clear_and_enter_last_name("pradhan")
    register_account_page.enter_email("will_smith123@gmail.com")
    register_account_page.enter_telephone("9178251492")
    register_account_page.enter_password("willsmith@123")
    register_account_page.select_yes_opt()
    register_account_page.click_agree()
    register_account_page.click_continue_button()
    time.sleep(3)
    register_account_page.verify_account_creation()
    register_account_page.click_continue_button2()
    time.sleep(3)
    register_account_page.click_order_history()
    # Step 2: Address
    address_page = AddressBookPage(driver)
    address_page.select_address_book_opt()
    address_page.select_new_address()