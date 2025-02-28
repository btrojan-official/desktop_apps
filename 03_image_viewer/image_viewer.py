from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


class ImageViewer(QGraphicsView):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Image Viewer")
        self.setGeometry(100, 100, 800, 600)
        
        self.center_window()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.open_button = QPushButton("Open Image")
        self.open_button.clicked.connect(self.open_image)
        layout.addWidget(self.open_button)
        
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.image_label)
        
        self.open_button.setStyleSheet("background-color: #4caf50; color: white; font-size: 16px; padding: 10px;")
        self.image_label.setStyleSheet("border: 2px solid #000; padding: 20px;")
        
    def open_image(self):
        file, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Image Files (*.png *.jpg *.jpeg *.gif *.bmp)")
        
        if file:
            pixmap = QPixmap(file)
            if not pixmap.isNull():
                self.image_label.setPixmap(pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio))
            
        
        
    def center_window(self):
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()
        
        window_width = self.width()
        window_height = self.height()
        
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        
        self.move(x, y)
        
if __name__ == "__main__":
    app = QApplication([])
    window = ImageViewer()
    window.show()
    app.exec_()