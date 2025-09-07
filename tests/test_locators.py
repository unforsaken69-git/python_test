from playwright.sync_api import sync_playwright

def test_locators():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, channel="chrome")
        page = browser.new_page()
        page.goto("https://letcode.in/edit")
        page.wait_for_selector("input[id='fullName']")
        page.locator("#fullName").fill("Playwright tutorial")
        page.locator("#join").press("End")
        page.locator("#join").type(" Human")
        check_text = page.locator("#join").input_value()
        print(f"check_text: {check_text}")
        # 等待並點擊結果

        browser.close()