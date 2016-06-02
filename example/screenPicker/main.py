import sys
from PyQt5 import QtCore, QtWidgets, QtQuick
from OpenGL import GL  # Fix execution shader bug
import quickmamba


if __name__ == '__main__':
    quickmamba.qmlRegister()
    app = QtWidgets.QApplication(sys.argv)
    view = QtQuick.QQuickView()
    view.setResizeMode(QtQuick.QQuickView.SizeRootObjectToView)
    # Create a declarative view
    view.setSource(QtCore.QUrl("source.qml"))

    view.show()
    app.exec_()
