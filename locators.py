from selenium.webdriver.common.by import By

# button_type_insurance = (By.XPATH, '//span[text()="Жизнь"]')
button_type_insurance = (By.XPATH, '//span[text()="Жизнь"]/parent::*')
button_bank_derop_list = (By.CSS_SELECTOR, '.MuiButtonBase-root.MuiIconButton-root.MuiAutocomplete-popupIndicator')
bank_input_field = (By.CSS_SELECTOR, '.MuiInputBase-input.MuiOutlinedInput-input.MuiAutocomplete-input')
input_bank_value = (By.CSS_SELECTOR, 'input[aria-activedescendant*="option-1"]')
button_clear_bank = (By.CSS_SELECTOR, '.MuiIconButton-root.MuiAutocomplete-clearIndicator')
input_credit = (By.CSS_SELECTOR, 'input[name=creditValue]')

# input_bank_value = (By.CSS_SELECTOR, '.MuiInputBase-input.MuiOutlinedInput-input.MuiAutocomplete-input')