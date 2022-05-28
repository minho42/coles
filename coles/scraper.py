import time
from playwright.sync_api import sync_playwright


def get_balance(card_number: str, pin: str):
    assert card_number
    assert 16 <= len(card_number) <= 20
    assert pin

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.giftcards.com.au/checkbalance")
        page.wait_for_selector('iframe[title="reCAPTCHA"]')

        page.fill("input#cardNumber", card_number)
        page.fill("input#cardPIN", pin)
        page.evaluate("document.querySelector('input#cardPIN').scrollIntoView();")
        page.frame_locator('iframe[title="reCAPTCHA"]').locator(".recaptcha-checkbox-border").click()
        time.sleep(2)

        # https://webscraping.pro/headless-chrome-detection-and-anti-detection/
        # Bypass headless chrome detection
        page.evaluate("Object.defineProperty(navigator, 'webdriver', { get: () => false });")
        webdriver = page.evaluate("navigator.webdriver")
        assert not webdriver, "navigator.webdriver not changed to false"

        page.locator("form#cbForm button").click()

        # https://www.giftcards.com.au/CheckBalance/TransactionHistory
        page.wait_for_selector(".gift-card-summary__rowBorder td")
        balance = page.query_selector(".gift-card-summary__rowBorder td").inner_text()
        # $0.00
        browser.close()
        print(f"{card_number}: {balance}")
        return balance.replace("$", "")


# card_mumber = "62734010074546419"
# pin = "3336"
# get_balance(card_mumber, pin)
