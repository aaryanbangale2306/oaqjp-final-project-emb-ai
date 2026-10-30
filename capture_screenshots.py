"""
Script to capture genuine browser screenshots of the running Emotion Detector web application.
Generates:
- 6b_deployment_test.png: Successful emotion detection on 'I think I am having fun'
- 7c_error_handling_interface.png: Error handling on blank input ('Invalid text! Please try again!')
"""

import time
from playwright.sync_api import sync_playwright


def capture_screenshots():
    """Captures real screenshots of the web application in Chrome."""
    with sync_playwright() as p:
        browser = p.chromium.launch(
            executable_path=r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            headless=True
        )
        context = browser.new_context(viewport={"width": 1280, "height": 800})
        page = context.new_page()

        # Step 1: 6b Deployment Test
        print("Navigating to http://127.0.0.1:5000/ ...")
        page.goto("http://127.0.0.1:5000/")
        page.wait_for_selector("#textToAnalyze")

        print("Entering test statement: 'I think I am having fun'")
        page.fill("#textToAnalyze", "I think I am having fun")
        page.click("button.btn.btn-secondary")

        print("Waiting for response in #system_response ...")
        page.wait_for_function(
            "document.getElementById('system_response').innerText.includes('dominant emotion')"
        )
        time.sleep(1)

        page.screenshot(path="6b_deployment_test.png")
        print("Successfully generated: 6b_deployment_test.png")

        # Step 2: 7c Error Handling Interface
        print("Clearing text to test error handling with blank input ...")
        page.fill("#textToAnalyze", "")
        page.click("button.btn.btn-secondary")

        print("Waiting for error message in #system_response ...")
        page.wait_for_function(
            "document.getElementById('system_response').innerText.includes('Invalid text')"
        )
        time.sleep(1)

        page.screenshot(path="7c_error_handling_interface.png")
        print("Successfully generated: 7c_error_handling_interface.png")

        browser.close()


if __name__ == "__main__":
    capture_screenshots()
