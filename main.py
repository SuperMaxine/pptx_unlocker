import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QWidget, QToolTip,
                             QPushButton, QApplication)
from PyQt5.QtGui import QIcon
import file
import surface

if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = surface.Ui_Form()
    ui.setupUi(widget)
    widget.setWindowIcon(QIcon(file.resource_path('pic/powerpoint.png')))  # 增加icon图标，如果没有图片可以没有这句
    widget.setFixedSize(400, 300)
    widget.show()
    sys.exit(app.exec_())
