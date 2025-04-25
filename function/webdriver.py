from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class WebDriverManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(WebDriverManager, cls).__new__(cls)
            cls._instance._initialize_driver()
        return cls._instance

    def _initialize_driver(self):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-extensions")
        self.service = Service()

        self.driver = webdriver.Chrome(service=self.service, options=chrome_options)

    def get_driver(self):
        return self.driver


