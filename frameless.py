#!/usr/bin/python3
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import sounddevice as sd
import speech_recognition as sr

def record_audio(duration,sample_rate = 44100):
    fs = sample_rate  # Sample rate
    seconds = duration  # Duration of recording
    
    print('Speak')
    myrecording = sd.rec(int(seconds * fs),fs,1)
    sd.wait()  # Wait until recording is finished
    print('Stop')
    #print(myrecording.flatten())
    #print(myrecording)

    '''write('output.wav', fs, myrecording)  # Save as WAV file 
    data, fs = sf.read('output.wav')
    print(data)
    sf.write('output.flac',data,fs)'''

    wavio.write('output.wav',myrecording,fs,sampwidth=2)



def recognise_speech(filename = 'output.wav'):
    r = sr.Recognizer()
    data = sr.AudioFile('output.wav')
    with data as source:
        audio = r.record(source)
    return (r.recognize_google(audio))

def speech_recognizer():
    record_audio(5)
    return recognise_speech()
 
CSS = \
{
    'QWidget':
    {
        'background-color': '#333333',
    },
    'QLabel#label':
    {
        'color': '#888888',
        'background-color': '#444444',
        'font-weight': 'bold',
    },
    'QLabel#label:active':
    {
        'color': '#1d90cd',
    },
    'QPushButton#button':
    {
        'color': '#888888',
        'background-color': '#444444',
        'font-weight': 'bold',
        'border': 'none',
        'padding': '5px',
    },
    'QPushButton#button:active':
    {
        'color': '#ffffff',
    },
    'QPushButton#button:hover':
    {
        'color': '#1d90cd',
    }
}
 
def dictToCSS(dictionnary):
    stylesheet = ""
    for item in dictionnary:
        stylesheet += item + "\n{\n"
        for attribute in dictionnary[item]:
            stylesheet += "  " + attribute + ": " + dictionnary[item][attribute] + ";\n"
        stylesheet += "}\n"
    return stylesheet
 
 
class Main(QtWidgets.QMainWindow):
    def __init__(self, parent):
        super().__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setStyleSheet(dictToCSS(CSS))
        self.resize(200, 150)
        self.ui = QtWidgets.QWidget(self)
        self.setCentralWidget(self.ui)
 
        self.ui.button = QtWidgets.QPushButton("Speak")
        self.ui.button.setObjectName("button")
        self.ui.button.clicked.connect(self.close)
        self.ui.button.setFocusPolicy(QtCore.Qt.NoFocus)
 
        self.ui.label = QtWidgets.QLabel("Nothing Spoken Yet")
        self.ui.label.setObjectName("label")
        self.ui.label.setAlignment(QtCore.Qt.AlignCenter)
 
        self.ui.layout = QtWidgets.QVBoxLayout()
        self.ui.layout.setContentsMargins(50, 50, 50, 50)
        self.ui.layout.addWidget(self.ui.button)
        self.ui.layout.addWidget(self.ui.label)
        self.ui.setLayout(self.ui.layout)
 
        self.show()
 
    def mouseMoveEvent(self, event):
        # Enable mouse dragging
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()
 
    def mousePressEvent(self, event):
        # Enable mouse dragging
        if event.button() == QtCore.Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()
 
    def keyPressEvent(self, event):
        # Escape key close the window
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()
        elif event.key() == QtCore.Qt.Key_Space:
            self.ui.button.setText('Please Speak')
        QtWidgets.QMainWindow.keyPressEvent(self, event)
 
    def paintEvent(self, event):
        # Draw a one pixel border
        borderColor = QtGui.QColor("black")
        bgColor = QtGui.QColor(self.palette().color(QtGui.QPalette.Background))
        painter = QtGui.QPainter(self)
        painter.setPen(QtCore.Qt.NoPen)
        painter.setBrush(QtGui.QBrush(borderColor))
        painter.drawRect(0, 0, self.width(), self.height())
        painter.setBrush(QtGui.QBrush(bgColor))
        painter.drawRect(1, 1, self.width()-2, self.height()-2)
 
 
if __name__== '__main__':
    app = QtWidgets.QApplication([])
    gui = Main(app)
    sys.exit(app.exec_())