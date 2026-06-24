from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QSystemTrayIcon,
    QMenu,
    QApplication,
    QStyle
)

from PySide6.QtGui import QAction

from tracking.tracker import Tracker

from config.sync_manager import (
    get_last_sync
)

from PySide6.QtCore import QTimer

class DashboardWindow(QWidget):

    def __init__(self, user_name):
        super().__init__()

        self.user_name = user_name

        # Exit handling flag
        self.is_exiting = False

        self.setWindowTitle("Dashboard")
        self.setGeometry(300, 200, 500, 300)

        self.tracker = Tracker()

        self.setup_ui()

        self.create_tray_icon()

        self.sync_timer = QTimer()

        self.sync_timer.timeout.connect(
            self.update_sync_label
        )

        self.sync_timer.start(5000)

    def setup_ui(self):

        layout = QVBoxLayout()

        welcome_label = QLabel(
            f"Welcome {self.user_name}!!"
        )

        self.status_label = QLabel(
            "Status : Stopped"
        )

        self.sync_label = QLabel(
        f"Last Sync : {get_last_sync()}"
        )

        self.start_button = QPushButton(
            "Start Tracking"
        )

        self.stop_button = QPushButton(
            "Stop Tracking"
        )

        layout.addWidget(welcome_label)
        layout.addWidget(self.status_label)
        layout.addWidget(self.sync_label)
        layout.addWidget(self.start_button)
        layout.addWidget(self.stop_button)

        self.setLayout(layout)

        # Connect buttons
        self.start_button.clicked.connect(
            self.start_tracking
        )

        self.stop_button.clicked.connect(
            self.stop_tracking
        )

    def start_tracking(self):

        if self.tracker.is_tracking:
            return

        self.start_button.setEnabled(False)

        self.tracker.start_tracking()

        self.status_label.setText(
            "Status : Tracking"
        )

    def stop_tracking(self):

        self.tracker.stop_tracking()

        self.start_button.setEnabled(True)

        self.status_label.setText(
            "Status : Stopped"
        )

    def create_tray_icon(self):
        self.tray_icon = QSystemTrayIcon(self)

        # icon
        icon = QApplication.style().standardIcon(
            QStyle.StandardPixmap.SP_FileDialogDetailedView
        )

        self.tray_icon.setIcon(icon)

        self.tray_icon.setToolTip(
            "Desktop Tracker"
        )

        tray_menu = QMenu()

        restore_action = QAction(
            "Restore",
            self
        )

        exit_action = QAction(
            "Exit",
            self
        )

        restore_action.triggered.connect(
            self.restore_window
        )

        exit_action.triggered.connect(
            self.exit_application
        )

        tray_menu.addAction(restore_action)
        tray_menu.addAction(exit_action)

        self.tray_icon.setContextMenu(
            tray_menu
        )

        # Double click tray icon → Restore
        self.tray_icon.activated.connect(
            self.on_tray_icon_activated
        )

        self.tray_icon.show()

    def on_tray_icon_activated(self, reason):

        if reason == QSystemTrayIcon.ActivationReason.DoubleClick:
            self.restore_window()

    def restore_window(self):

        self.show()

        self.showNormal()

        self.raise_()

        self.activateWindow()

    def exit_application(self):

        self.is_exiting = True

        try:
            self.tracker.stop_tracking()
        except Exception as e:
            print("Tracker Stop Error:", e)

        self.tray_icon.hide()

        self.close()

    def closeEvent(self, event):

        # Real Exit
        if self.is_exiting:
            event.accept()
            return

        # Minimize to Tray
        event.ignore()

        self.hide()

        self.tray_icon.showMessage(
            "Desktop Tracker",
            "Application minimized to system tray."
        )


    def update_sync_label(self):

        self.sync_label.setText(
            f"Last Sync : {get_last_sync()}"
        )