import sys
from custome_errors import *
sys.excepthook = my_excepthook
from fpdf import fpdf
import update
import gui
import guiTools
from settings import *
import PyQt6.QtWidgets as qt
import PyQt6.QtGui as qt1
import PyQt6.QtCore as qt2
language.init_translation()
class main (qt.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(app.name + _("version : ") + str(app.version))
        self.pdf=fpdf.FPDF()
        layout=qt.QVBoxLayout()
        self.add=qt.QPushButton(_("Add"))
        self.add.setDefault(True)
        self.add.clicked.connect(self.on_add)
        layout.addWidget(self.add)
        self.save=qt.QPushButton(_("save"))
        self.save.setDefault(True)
        self.save.clicked.connect(self.on_save)
        layout.addWidget(self.save)
        self.setting=qt.QPushButton(_("settings"))
        self.setting.setDefault(True)
        self.setting.clicked.connect(lambda: settings(self).exec())
        layout.addWidget(self.setting)
        w=qt.QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)

        mb=self.menuBar()
        help=mb.addMenu(_("help"))
        helpFile=qt1.QAction(_("help file"),self)
        help.addAction(helpFile)
        helpFile.triggered.connect(lambda:guiTools.HelpFile())
        helpFile.setShortcut("f1")
        cus=help.addMenu(_("contact us"))
        telegram=qt1.QAction("telegram",self)
        cus.addAction(telegram)
        telegram.triggered.connect(lambda:guiTools.OpenLink(self,"https://t.me/mesteranasm"))
        telegramc=qt1.QAction(_("telegram channel"),self)
        cus.addAction(telegramc)
        telegramc.triggered.connect(lambda:guiTools.OpenLink(self,"https://t.me/tprogrammers"))
        githup=qt1.QAction(_("Github"),self)
        cus.addAction(githup)
        githup.triggered.connect(lambda: guiTools.OpenLink(self,"https://Github.com/mesteranas"))
        X=qt1.QAction(_("x"),self)
        cus.addAction(X)
        X.triggered.connect(lambda:guiTools.OpenLink(self,"https://x.com/mesteranasm"))
        email=qt1.QAction(_("email"),self)
        cus.addAction(email)
        email.triggered.connect(lambda: guiTools.sendEmail("anasformohammed@gmail.com","project_type=GUI app={} version={}".format(app.name,app.version),""))
        Github_project=qt1.QAction(_("visite project on Github"),self)
        help.addAction(Github_project)
        Github_project.triggered.connect(lambda:guiTools.OpenLink(self,"https://Github.com/mesteranas/{}".format(settings_handler.appName)))
        Checkupdate=qt1.QAction(_("check for update"),self)
        help.addAction(Checkupdate)
        Checkupdate.triggered.connect(lambda:update.check(self))
        licence=qt1.QAction(_("license"),self)
        help.addAction(licence)
        licence.triggered.connect(lambda: Licence(self))
        donate=qt1.QAction(_("donate"),self)
        help.addAction(donate)
        donate.triggered.connect(lambda:guiTools.OpenLink(self,"https://www.paypal.me/AMohammed231"))
        about=qt1.QAction(_("about"),self)
        help.addAction(about)
        about.triggered.connect(lambda:qt.QMessageBox.information(self,_("about"),_("{} version: {} description: {} developer: {}").format(app.name,str(app.version),app.description,app.creater)))
        self.setMenuBar(mb)
        if settings_handler.get("update","autoCheck")=="True":
            update.check(self,message=False)
    def closeEvent(self, event):
        if settings_handler.get("g","exitDialog")=="True":
            m=guiTools.ExitApp(self)
            m.exec()
            if m:
                event.ignore()
        else:
            self.close()
    def on_add(self):
        menu=qt.QMenu(self)
        text=qt1.QAction(_("add text"),self)
        text.triggered.connect(self.on_add_text)
        link=qt1.QAction(_("add link"),self)
        link.triggered.connect(self.on_add_link)
        image=qt1.QAction(_("add image"),self)
        image.triggered.connect(self.on_add_image)
        menu.addActions([text,link,image])
        menu.exec()
    def on_save(self):
        file=qt.QFileDialog(self)
        file.setAcceptMode(file.AcceptMode.AcceptSave)
        if file.exec()==file.DialogCode.Accepted:
            self.pdf.output(file.selectedFiles()[0])
            qt.QMessageBox.information(self,_("done"),_("saved"))
    def on_add_text(self):
        text,ok=qt.QInputDialog.getText(self,_("add text"),_("text"))
        if ok:
            w,ok=qt.QInputDialog.getDouble(self,_("add text"),_("inter width"),500,10,5000)
            if ok:
                h,ok=qt.QInputDialog.getDouble(self,_("add text"),_("inter hight"),500,10,5000)
                if ok:
                    self.pdf.set_font(family="Arial")
                    self.pdf.cell(h=h,w=w,txt=text)
                    qt.QMessageBox.information(self,_("done"),_("text added"))
    def on_add_link(self):
        text,ok=qt.QInputDialog.getText(self,_("add text"),_("text"))
        if ok:
            w,ok=qt.QInputDialog.getDouble(self,_("add text"),_("inter width"),500,10,5000)
            if ok:
                h,ok=qt.QInputDialog.getDouble(self,_("add text"),_("inter hight"),500,10,5000)
                if ok:
                    link,ok=qt.QInputDialog.getText(self,_("add text"),_("link"))
                    if ok:
                        self.pdf.set_font(family="Arial")
                        self.pdf.cell(h=h,w=w,txt=text,link=link)
                        qt.QMessageBox.information(self,_("done"),_("link added"))
    def on_add_image(self):
        file=qt.QFileDialog(self)
        if file.exec()==file.DialogCode.Accepted:
            w,ok=qt.QInputDialog.getDouble(self,_("add text"),_("inter width"),500,10,5000)
            if ok:
                h,ok=qt.QInputDialog.getDouble(self,_("add text"),_("inter hight"),500,10,5000)
                if ok:
                    self.pdf.set_font(family="Arial",size=20)
                    self.pdf.image(name=file.selectedFiles()[0],w=w,h=h)
                    qt.QMessageBox.information(self,_("done"),_("image added"))

App=qt.QApplication([])
w=main()
w.show()
App.setStyle('fusion')
App.exec()