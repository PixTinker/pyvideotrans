# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'videoandaudio.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import (QMetaObject, QSize, Qt)
from PySide6.QtGui import (QCursor)
from PySide6.QtWidgets import (QHBoxLayout, QLabel, QLineEdit,
                               QPushButton,
                               QVBoxLayout, QCheckBox)

from videotrans.configure import config


class Ui_videoandaudio(object):
    def setupUi(self, videoandaudio):
        if not videoandaudio.objectName():
            videoandaudio.setObjectName(u"videoandaudio")
        videoandaudio.resize(643, 300)
        videoandaudio.setWindowModality(QtCore.Qt.NonModal)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(videoandaudio.sizePolicy().hasHeightForWidth())
        videoandaudio.setSizePolicy(sizePolicy)
        videoandaudio.setMaximumSize(QtCore.QSize(643, 300))


        self.horizontalLayout_3 = QHBoxLayout(videoandaudio)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.folder = QLineEdit(videoandaudio)
        self.folder.setObjectName(u"folder")
        self.folder.setMinimumSize(QSize(0, 35))
        self.folder.setReadOnly(True)

        self.labeltips=QLabel(videoandaudio)


        self.horizontalLayout.addWidget(self.folder)

        self.videobtn = QPushButton(videoandaudio)
        self.videobtn.setObjectName(u"videobtn")
        self.videobtn.setMinimumSize(QSize(180, 35))
        self.videobtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.videobtn.setMouseTracking(False)
        self.horizontalLayout.addWidget(self.videobtn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.labeltips)

        self.startbtn = QPushButton(videoandaudio)
        self.startbtn.setObjectName(u"startbtn")
        self.startbtn.setMinimumSize(QSize(150, 35))
        self.startbtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.remain=QCheckBox(videoandaudio)
        self.remain.setChecked(False)


        self.h2=QHBoxLayout()
        self.h2.addStretch()
        self.h2.addWidget(self.remain)
        self.h2.addWidget(self.startbtn)
        self.h2.addStretch()

        self.verticalLayout.addLayout(self.h2)


        self.resultbtn = QPushButton(videoandaudio)
        self.resultbtn.setObjectName(u"resultbtn")
        self.resultbtn.setStyleSheet("""background-color:transparent""")
        self.resultbtn.setMinimumSize(QSize(0, 30))
        self.resultbtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.loglabel=QLabel(videoandaudio)
        self.loglabel.setStyleSheet('''color:#148cd2''')
        self.verticalLayout.addWidget(self.resultbtn)
        self.verticalLayout.addWidget(self.loglabel)
        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.retranslateUi(videoandaudio)

        QMetaObject.connectSlotsByName(videoandaudio)


    def retranslateUi(self, videoandaudio):
        videoandaudio.setWindowTitle("批量视频音频合并" if config.defaulelang == 'zh' else 'Batch video and audio merger')
        self.folder.setPlaceholderText(
            "选择要合并的视频音频所在文件夹" if config.defaulelang == 'zh' else 'Select the folder where you want to merge the video and audio')
        self.videobtn.setText("选择文件夹" if config.defaulelang == 'zh' else 'Select the folder')
        self.startbtn.setText("开始执行" if config.defaulelang == 'zh' else 'Start of execution')
        self.resultbtn.setText("打开保存结果目录" if config.defaulelang == 'zh' else 'Open the save results directory')
        self.labeltips.setText("将把所选文件夹内同名的视频和音频进行合并，例如 1.mp4和 1.wav" if config.defaulelang == 'zh' else 'Will merge video and audio with the same name in that folder, e.g. 1.mp4 and 1.wav')
        self.remain.setText('保留视频中原声音' if config.defaulelang=='zh' else 'Preserve the original sound in the video')
