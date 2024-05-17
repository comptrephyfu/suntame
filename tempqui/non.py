def remove_metamask(driver):
    """
    Remove Metamask extension from the browser.

    Args:
        driver (webdriver): The webdriver instance.
    """
    driver.get("chrome://extensions/")
    time.sleep(5)
    driver.find_element(By.XPATH, "//div[contains(@id, 'metamask-extension')]//button").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//button[@id='extension-settings-uninstall-button']").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//button[@id='extension-settings-uninstall-confirm']").click()
    time.sleep(5)

