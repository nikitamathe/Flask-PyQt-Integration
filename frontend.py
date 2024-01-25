import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
from PyQt5.QtCore import Qt, QUrl

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('PyQt Frontend')

        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)

        label = QLabel('Message from Flask API:', self)
        layout.addWidget(label)

        message_label = QLabel('', self)
        layout.addWidget(message_label)

        button = QPushButton('Get Message', self)
        button.clicked.connect(self.get_message)
        layout.addWidget(button)

        self.setCentralWidget(central_widget)

    def get_message(self):
        url = 'http://127.0.0.1:8000/api/hello'  # Replace with your Flask API URL
        manager = QNetworkAccessManager(self)
        request = QNetworkRequest(QUrl(url))
        reply = manager.get(request)
        reply.finished.connect(lambda: self.handle_reply(reply))

    def handle_reply(self, reply):
        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll().data().decode('utf-8')
            self.show_message(data)
        else:
            self.show_message('Error fetching data')

        reply.deleteLater()

    def show_message(self, message):
        central_widget = self.centralWidget()
        message_label = central_widget.findChild(QLabel)
        message_label.setText(message)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
