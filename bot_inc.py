import sys
import time
import webbrowser
from PyQt5 import QtWidgets
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.iurl = QtWidgets.QLineEdit()
        self.iurl.setPlaceholderText("Your Youtube Link is Here")
        self.itekrar = QtWidgets.QLineEdit()
        self.itekrar.setPlaceholderText("Repeat")
        self.ibaslat = QtWidgets.QPushButton("START")
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.iurl)
        vbox.addWidget(self.itekrar)
        vbox.addWidget(self.ibaslat)
        vbox.addStretch()
        self.setLayout(vbox)
        self.ibaslat.clicked.connect(self.fbasla)
        self.show()

    def fbasla(self):
        url = self.iurl.text()
        tekrar = int(self.itekrar.text())

        """
        proxy_options = webdriver.ChromeOptions()
        proxy_options.add_argument('--proxy-server=http://your-proxy-server-url:port')  # proxy adresses add here

        driver = webdriver.Chrome(options=proxy_options)
        """

        driver = webdriver.Chrome() # after add proxy delete this the row

        for i in range(tekrar):
            driver.get(url)
            time.sleep(15)  # new private browser will open X seconds later

            wait = WebDriverWait(driver, 10)  # browser will close X seconds later
            wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'body'))).send_keys('w')

        driver.quit()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    pencere = Pencere()
    sys.exit(app.exec_())


# http://tiny.cc/bn0cvz