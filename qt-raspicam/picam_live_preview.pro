#-------------------------------------------------
#
# Project created by QtCreator 2017-03-22T20:19:05
#
#-------------------------------------------------

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = picam-live
TEMPLATE = app


SOURCES += main.cpp\
        mainwindow.cpp \
    cameraworker.cpp

HEADERS  += mainwindow.h \
    cameraworker.h

FORMS    += mainwindow.ui

INCLUDEPATH += /Users/Jarrey/raspi/sysroot/usr/local/include

SYSROOT = /Volumes/xtool-build-env/armv8-rpi3-linux-gnueabihf/armv8-rpi3-linux-gnueabihf/sysroot

# Requirements for raspicam
LIBS += -L$$SYSROOT/opt/vc/lib -lmmal -lmmal_core -lmmal_util
LIBS += -L$$SYSROOT/usr/local/lib -I$$SYSROOT/usr/local/include -lraspicam

DISTFILES += \
    .astylerc


# Default rules for deployment.
qnx: target.path = /tmp/$${TARGET}/bin
else: unix:!android: target.path = /home/pi/$${TARGET}/bin
!isEmpty(target.path): INSTALLS += target
