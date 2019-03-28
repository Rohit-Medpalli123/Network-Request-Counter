# import selenium webdriver(which allows us browser automation)
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


class BrowserAutomation:
    def __init__(self,parser):
        self.parser = parser
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

    def visit_url(self):
        """This function visits a particular url mentioned in config file"""
        self.required_url = self.parser.get('URL', 'website')
        self.driver.get(self.required_url )
        self.driver.maximize_window()

    def resource_timing_api(self):
        """This function provides detailed network timing data"""
        self.tracker_list = self.driver.execute_script(""" 
                    return window.performance.getEntriesByType("resource")""")
        return self.tracker_list

    def close_browser(self):
        """This function closes the browser once the operation is completed"""
        self.driver.quit()
