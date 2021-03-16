from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QLabel, QLineEdit, QProgressBar, \
    QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QDialogButtonBox
from PyQt5.QtCore import Qt, QBasicTimer, QThread, QRect
import sys


class ProgressBar(QDialog):
    def __init__(self, parent=None):
        super(ProgressBar, self).__init__(parent)

        # Qdialog窗体的设置
        self.resize(500, 32)  # QDialog窗的大小

        # 创建并设置 QProcessbar
        self.progressBar = QProgressBar(self)  # 创建
        self.progressBar.setMinimum(0)  # 设置进度条最小值
        self.progressBar.setMaximum(100)  # 设置进度条最大值
        self.progressBar.setValue(0)  # 进度条初始值为0
        self.progressBar.setGeometry(QRect(1, 3, 499, 28))  # 设置进度条在 QDialog 中的位置 [左，上，右，下]
        self.show()

    def setValue(self, task_number, total_task_number, value):  # 设置总任务进度和子任务进度
        if task_number == '0' and total_task_number == '0':
            self.setWindowTitle(self.tr('正在处理中'))
        else:
            label = "正在处理：" + "第" + str(task_number) + "/" + str(total_task_number) + '个任务'
            self.setWindowTitle(self.tr(label))  # 顶部的标题
        self.progressBar.setValue(value)


class pyqtbar():
    '''
    task_number和 total_task_number都为 0 时，不显示当前进行的任务情况
    task_number<total_task_number 都为整数，错误的设置将出现错误显示，暂未设置报错警告

    # 使用示例
    import time
    bar = pyqtbar() # 创建实例
    total_number=10
    # 任务1
    task_id=1
    for process in range(1, 100):
        time.sleep(0.05)
        bar.set_value(task_id,total_number,process) # 刷新进度条
    # 任务2
    task_id = 2
    for process in range(1, 100):
        time.sleep(0.05)
        bar.set_value(task_id, total_number,process)
    bar.close # 关闭 bar 和 app
    '''

    def __init__(self):
        # self.app = QApplication(sys.argv)  # 打开系统 app
        self.progressbar = ProgressBar()  # 初始化 ProcessBar实例

    def set_value(self, task_number, total_task_number, i):
        self.progressbar.setValue(str(task_number), str(total_task_number), i + 1)  # 更新进度条的值
        QApplication.processEvents()  # 实时刷新显示

    @property
    def close(self):
        self.progressbar.close()  # 关闭进度条
        # self.app.exit()  # 关闭系统 app