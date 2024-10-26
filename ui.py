from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QPoint
from main import GoogleScraper


class Ui_Scraper(object):
    def setupUi(self, Scraper):
        Scraper.setObjectName("Scraper")
        Scraper.setWindowFlags(Qt.FramelessWindowHint)  # Remove default window frame
        Scraper.setAttribute(Qt.WA_TranslucentBackground)  # Transparent background for rounded corners
        Scraper.resize(500, 500)

        # Main Widget (custom background)
        self.centralwidget = QtWidgets.QWidget(Scraper)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: #2b2b2b; border-radius: 15px;")  # Darker, softer background

        # Custom Title Bar
        self.title_bar = QtWidgets.QWidget(self.centralwidget)
        self.title_bar.setGeometry(QtCore.QRect(0, 0, 500, 40))
        self.title_bar.setStyleSheet(
            "background-color: #3a3a3a; border-top-left-radius: 15px; border-top-right-radius: 15px;")
        self.title_bar.setObjectName("title_bar")

        self.close_button = QtWidgets.QPushButton(self.title_bar)
        self.close_button.setGeometry(QtCore.QRect(460, 10, 30, 30))
        self.close_button.setStyleSheet(
            "background-color: #d9534f; border-radius: 15px; color: white; font-weight: bold;")
        self.close_button.setText("X")
        self.close_button.clicked.connect(Scraper.close)

        self.minimize_button = QtWidgets.QPushButton(self.title_bar)
        self.minimize_button.setGeometry(QtCore.QRect(420, 10, 30, 30))
        self.minimize_button.setStyleSheet(
            "background-color: #f0ad4e; border-radius: 15px; color: white; font-weight: bold;")
        self.minimize_button.setText("_")
        self.minimize_button.clicked.connect(Scraper.showMinimized)

        # Title Text (More subtle color and font size)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 20, 300, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #f0f0f0;")  # Soft white text without glow
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setText("Easy ScraperV1")
        self.label.setObjectName("label")

        # Other UI Elements (same as before but with toned-down colors)
        self.label_keyword = QtWidgets.QLabel(self.centralwidget)
        self.label_keyword.setGeometry(QtCore.QRect(50, 80, 150, 30))
        self.label_keyword.setFont(QtGui.QFont("Arial", 11))
        self.label_keyword.setStyleSheet("color: #f0f0f0;")
        self.label_keyword.setText("Enter keyword:")
        self.label_keyword.setObjectName("label_keyword")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(220, 80, 200, 30))
        self.lineEdit.setStyleSheet("""
            font: 11pt 'Arial'; 
            padding: 5px; 
            background-color: #404040;
            color: #f0f0f0;
            border: 2px solid #555555; 
            border-radius: 5px;
        """)
        self.lineEdit.setObjectName("lineEdit")

        self.label_engine = QtWidgets.QLabel(self.centralwidget)
        self.label_engine.setGeometry(QtCore.QRect(50, 130, 150, 30))
        self.label_engine.setFont(QtGui.QFont("Arial", 11))
        self.label_engine.setStyleSheet("color: #f0f0f0;")
        self.label_engine.setText("Search engine:")
        self.label_engine.setObjectName("label_engine")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(220, 130, 200, 30))
        self.comboBox.setStyleSheet("""
            font: 11pt 'Arial'; 
            padding: 5px; 
            background-color: #404040;
            color: #f0f0f0;
            border: 2px solid #555555; 
            border-radius: 5px;
        """)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Google")
        self.comboBox.addItem("Bing")

        self.label_choice = QtWidgets.QLabel(self.centralwidget)
        self.label_choice.setGeometry(QtCore.QRect(50, 180, 150, 30))
        self.label_choice.setFont(QtGui.QFont("Arial", 11))
        self.label_choice.setStyleSheet("color: #f0f0f0;")
        self.label_choice.setText("Scrape:")
        self.label_choice.setObjectName("label_choice")

        self.radio_url = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_url.setGeometry(QtCore.QRect(220, 180, 80, 30))
        self.radio_url.setText("URLs")
        self.radio_url.setFont(QtGui.QFont("Arial", 11))
        self.radio_url.setStyleSheet("color: #f0f0f0;")
        self.radio_url.setChecked(True)

        self.radio_image = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_image.setGeometry(QtCore.QRect(310, 180, 80, 30))
        self.radio_image.setText("Images")
        self.radio_image.setFont(QtGui.QFont("Arial", 11))
        self.radio_image.setStyleSheet("color: #f0f0f0;")

        self.label_pages = QtWidgets.QLabel(self.centralwidget)
        self.label_pages.setGeometry(QtCore.QRect(50, 230, 300, 30))
        self.label_pages.setFont(QtGui.QFont("Arial", 11))
        self.label_pages.setStyleSheet("color: #f0f0f0;")
        self.label_pages.setText("Pages to scrape:")
        self.label_pages.setObjectName("label_pages")

        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(220, 270, 100, 30))
        self.spinBox.setStyleSheet("""
            font: 11pt 'Arial'; 
            padding: 5px; 
            background-color: #404040;
            color: #f0f0f0;
            border: 2px solid #555555; 
            border-radius: 5px;
        """)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(50)
        self.spinBox.setObjectName("spinBox")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 350, 120, 40))
        self.pushButton.setStyleSheet("""
            font: bold 11pt 'Arial'; 
            background-color: #5bc0de; 
            color: white; 
            border-radius: 5px;
            padding: 10px;
        """)
        self.pushButton.setText("Run Scraper")
        self.pushButton.setObjectName("pushButton")

        # Hover effect for the button
        self.pushButton.setStyleSheet("""
            QPushButton {
                font: bold 11pt 'Arial'; 
                background-color: #5bc0de; 
                color: white; 
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #39b3d7;
            }
        """)

        self.pushButton.clicked.connect(self.run_scraper)

        self.radio_url.toggled.connect(self.toggle_scrape_options)
        self.radio_image.toggled.connect(self.toggle_scrape_options)

        Scraper.setCentralWidget(self.centralwidget)

        # Adding moving functionality
        self.title_bar.mousePressEvent = self.mouse_press_event
        self.title_bar.mouseMoveEvent = self.mouse_move_event

        self.dragPos = QPoint()

        self.retranslateUi(Scraper)
        QtCore.QMetaObject.connectSlotsByName(Scraper)

    def retranslateUi(self, Scraper):
        _translate = QtCore.QCoreApplication.translate
        Scraper.setWindowTitle(_translate("Scraper", "Scraper"))

    def run_scraper(self):
        search_engine = self.comboBox.currentText()
        query = self.lineEdit.text()
        n_of_pages_or_images = self.spinBox.value()
        scrape_type = "URLs" if self.radio_url.isChecked() else "Images"
        GoogleScraper.run(GoogleScraper(), query, search_engine, n_of_pages_or_images, scrape_type)

    def toggle_scrape_options(self):
        if self.radio_url.isChecked():
            self.label_pages.setText("Pages to scrape:")
            self.spinBox.setMaximum(50)
        else:
            self.label_pages.setText("Images to scrape:")
            self.spinBox.setMaximum(100)

    def mouse_press_event(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPos = event.globalPos()

    def mouse_move_event(self, event):
        if event.buttons() == Qt.LeftButton:
            Scraper.move(Scraper.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Scraper = QtWidgets.QMainWindow()
    ui = Ui_Scraper()
    ui.setupUi(Scraper)
    Scraper.show()
    sys.exit(app.exec_())
