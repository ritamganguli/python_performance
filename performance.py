import time
import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions

username = "shubhamr"  # Replace the username
access_key = "xyz"  # Replace the access key

options = ChromeOptions()
options.browser_version = "latest"
options.platform_name = "win10"
lt_options = {}
lt_options["username"] = username
lt_options["accessKey"] = access_key
lt_options["video"] = True
lt_options["resolution"] = "1920x1080"
lt_options["network"] = True
lt_options["smartWait"] = 60
lt_options["project"] = "unit_testing"
lt_options["name"] = "basic_unit_selinium"
lt_options["w3c"] = True
lt_options["plugin"] = "python-python"
lt_options["selenium_version"]="4.18.0"
lt_options['goog:loggingPrefs'] = {'performance': 'ALL'}  # Add logging preferences here
options.set_capability("LT:Options", lt_options)

class FirstSampleTest(unittest.TestCase):
    driver = None

    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor="https://{}:{}@hub.lambdatest.com/wd/hub".format(
                username, access_key
            ),
            options=options,
        )

    # """ You can write the test cases here """
    def test_demo_site(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.set_page_load_timeout(30)
        driver.set_window_size(1920, 1080)

        # Url
        print("Loading URL")
        driver.get("https://accounts.lambdatest.com/login")
        performance_logs = driver.get_log("performance")
        print("Performance Logs:")
        for log in performance_logs:
            print(log)

        # Let's click on an element
        time.sleep(30)
        print("Ending the test........")

    # tearDown runs after each test case
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
