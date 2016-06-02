import sys
from quickmamba.utils.instantcoding import QmlInstantCoding, ReloadComponent
from PyQt5 import QtCore, QtWidgets, QtQuick, QtQml
import os


def main():
    app = QtWidgets.QApplication(sys.argv)
    view = QtQuick.QQuickView()
    view.setResizeMode(QtQuick.QQuickView.SizeRootObjectToView)

    # Create a declarative view
    component = QtQml.QQmlComponent(view)
    topLevelItem = component.create()
    qmlFile = QtCore.QUrl("source.qml")
    view.setSource(qmlFile)

    # Declare we are using instant coding tool on this view
    qic = QmlInstantCoding(view, ReloadComponent(qmlFile, component, topLevelItem), verbose=True)
    
    # Add any source file (.qml and .js by default) in current working directory
    qic.addFilesFromDirectory(os.getcwd())

    view.show()
    app.exec_()

if __name__ == '__main__':
    main()
