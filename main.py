from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel

# Import the necessary QR code scanner library
from plyer import qrscanner

# Load the KV file
Builder.load_string('''
<QRScannerApp>:
    orientation: 'vertical'

    MDLabel:
        id: qr_data_label
        text: root.qr_data
        halign: 'center'
        valign: 'middle'
        size_hint_y: 0.5

    MDRaisedButton:
        text: 'Scan QR Code'
        on_release: app.scan_qr_code()
''')


class QRScannerApp(BoxLayout):
    qr_data = StringProperty("Scan a QR Code")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def process_qr(self, result, *args):
        if result:
            self.qr_data = result

    def scan_qr_code(self):
        qrscanner.scan(self.process_qr)


class MainApp(MDApp):
    def build(self):
        return QRScannerApp()


if __name__ == '__main__':
    MainApp().run()
