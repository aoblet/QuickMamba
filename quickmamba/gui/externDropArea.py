from PyQt5 import QtCore, QtGui
from PyQt5 import QtQuick


class ExternDropArea(QtQuick.QQuickItem):
    # QGraphicsSceneDragDropEvent:
    # Qt::MouseButtons buttons, Qt::DropAction dropAction,
    # const QMimeData mimeData, Qt::KeyboardModifiers modifiers,
    # QPointF pos, Qt::DropActions possibleActions, Qt::DropAction proposedAction, QWidget source
    internDragEnter = QtCore.pyqtSignal(
        bool, str,  # text
        bool, str,  # html
        bool, str,  # urls
        QtCore.Qt.MouseButtons, QtCore.Qt.DropAction,
        QtCore.Qt.KeyboardModifiers, QtCore.QPointF,
        QtCore.Qt.DropActions, QtCore.Qt.DropAction,
        str)
    internDragMove = QtCore.pyqtSignal(
        bool, str,  # text
        bool, str,  # html
        bool, str,  # urls
        QtCore.Qt.MouseButtons, QtCore.Qt.DropAction,
        QtCore.Qt.KeyboardModifiers, QtCore.QPointF,
        QtCore.Qt.DropActions, QtCore.Qt.DropAction,
        str)
    internDragLeave = QtCore.pyqtSignal(
        bool, str,  # text
        bool, str,  # html
        bool, str,  # urls
        QtCore.Qt.MouseButtons, QtCore.Qt.DropAction,
        QtCore.Qt.KeyboardModifiers, QtCore.QPointF,
        QtCore.Qt.DropActions, QtCore.Qt.DropAction,
        str)
    internDrop = QtCore.pyqtSignal(
        bool, str,  # text
        bool, str,  # html
        bool, str,  # urls
        QtCore.Qt.MouseButtons, QtCore.Qt.DropAction,
        QtCore.Qt.KeyboardModifiers, QtCore.QPointF,
        QtCore.Qt.DropActions, QtCore.Qt.DropAction,
        str)

    def __init__(self, parent=None):
        super(ExternDropArea, self).__init__(parent)
        #self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        urls = event.mimeData().urls()
        firstUrl = urls[0].toLocalFile() if len(urls) else '' \
                                                           ''
        self.internDragEnter.emit(
            event.mimeData().hasText(), event.mimeData().text(),
            event.mimeData().hasHtml(), event.mimeData().html(),
            event.mimeData().hasUrls(), firstUrl,
            #event.mimeData().hasImage(), event.mimeData().imageData(),
            #event.mimeData().hasColor(), event.mimeData().colorData(),
            
            event.buttons(), event.dropAction(),
            event.modifiers(), event.pos(),
            event.possibleActions(), event.proposedAction(),
            "")
            #event.source().accessibleName() if event.source() else "")

        if self._acceptDropValue:
            event.acceptProposedAction()
            self.setCursor(QtCore.Qt.DragMoveCursor)

        event.setAccepted(self._acceptDropValue)

    def dragMoveEvent(self, event):
        urls = event.mimeData().urls()
        firstUrl = urls[0].toLocalFile() if len(urls) else ''

        self.internDragMove.emit(
            event.mimeData().hasText(), event.mimeData().text(),
            event.mimeData().hasHtml(), event.mimeData().html(),
            event.mimeData().hasUrls(), firstUrl,
            #event.mimeData().hasImage(), event.mimeData().imageData(),
            #event.mimeData().hasColor(), event.mimeData().colorData(),

            event.buttons(), event.dropAction(),
            event.modifiers(), event.pos(),
            event.possibleActions(), event.proposedAction(),
            "")
            #event.source().accessibleName() if event.source() else "")

        event.setAccepted(self._acceptDropValue)

    def dragLeaveEvent(self, event):
        urls = event.mimeData().urls()
        firstUrl = urls[0].toLocalFile() if len(urls) else ""

        self.internDragLeave.emit(
            event.mimeData().hasText(), event.mimeData().text(),
            event.mimeData().hasHtml(), event.mimeData().html(),
            event.mimeData().hasUrls(), firstUrl,
            #event.mimeData().hasImage(), event.mimeData().imageData(),
            #event.mimeData().hasColor(), event.mimeData().colorData(),
            
            event.buttons(), event.dropAction(),
            event.modifiers(), event.pos(),
            event.possibleActions(), event.proposedAction(),
            "")
            #event.source().accessibleName() if event.source() else "")
        
        event.setAccepted(self._acceptDropValue)
        self.unsetCursor()

    def dropEvent(self, event):
        # hasText()  text()      text/plain
        # hasHtml()  html()      text/html
        # hasUrls()  urls()      text/uri-list
        # hasImage() imageData() image/ *
        # hasColor() colorData() application/x-color
        
        urls = event.mimeData().urls()
        firstUrl = urls[0].toLocalFile() if len(urls) else ""

        # creates a seg. fault at the end of the application,
        # if event.source() is called.
        #print "event source:", event.source()

        self.internDrop.emit(
            event.mimeData().hasText(), event.mimeData().text(),
            event.mimeData().hasHtml(), event.mimeData().html(),
            event.mimeData().hasUrls(), firstUrl,
            #event.mimeData().hasImage(), event.mimeData().imageData(),
            #event.mimeData().hasColor(), event.mimeData().colorData(),
            
            event.buttons(), event.dropAction(),
            event.modifiers(), event.pos(),
            event.possibleActions(), event.proposedAction(),
            "")
            #event.source().accessibleName() if event.source() else "")

        if self._acceptDropValue:
            event.acceptProposedAction()
            #print 'text:', event.mimeData().hasText(), event.mimeData().text()
            #print 'html:', event.mimeData().hasHtml(), event.mimeData().html()
            #print 'url:', event.mimeData().hasUrls(), [u.toLocalFile() for u in event.mimeData().urls()]

        event.setAccepted(self._acceptDropValue)
        self.unsetCursor()

    def getAcceptDrop(self):
        return self._acceptDropValue

    def setAcceptDrop(self, acceptDrop):
        self._acceptDropValue = acceptDrop
        self.update()
        self.acceptDropChanged.emit()

    acceptDropChanged = QtCore.pyqtSignal()
    _acceptDropValue = True
    acceptDrop = QtCore.pyqtProperty(bool, getAcceptDrop, setAcceptDrop, notify=acceptDropChanged)

