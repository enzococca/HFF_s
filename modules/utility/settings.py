#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
/***************************************************************************
        HFF_system Plugin  - A QGIS plugin to manage archaeological dataset
                             stored in Postgres
                             -------------------
    begin                : 2007-12-01
    copyright            : (C) 2008 by Luca Mandolesi
    email                : mandoluca at gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os
import traceback
import sys
from builtins import object
from qgis.PyQt.QtWidgets import *
from qgis.core import QgsMessageLog, Qgis, QgsSettings
from builtins import object
from .hff_system__OS_utility import Hff_OS_Utility


class Settings(object):
    SERVER = ""
    HOST = ""
    DATABASE = ""
    PASSWORD = ""
    PORT = ""
    USER = ""
    THUMB_PATH = ""
    THUMB_RESIZE = ""
    SITE_SET = ""
    LOGO = ""
    RESOURCES_PATH = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, 'resources')
    OS_UTILITY = Hff_OS_Utility()
    HOME = os.environ['HFF_HOME']
    path_rel = os.path.join(os.sep, HOME, 'HFF_DB_folder', 'config.cfg')
    
    conf = open( path_rel, "rb+")

    data = conf.read()

    text = (b'THUMB_RESIZE')
    text_a = (b'SITE_SET')
    text_b = (b'LOGO')

    if text in data:
        pass
    else:
        conf.seek(-3, 2)
        conf.read(1)
        conf.write(b"','THUMB_RESIZE' : ''")

    if text_a in data:
        pass
    else:
        conf.seek(-3, 2)
        conf.read(1)
        conf.write(b"','SITE_SET' : ''")
        
    if text_b in data:
        pass
    else:
        conf.seek(-3, 2)
        conf.read(1)
        conf.write(b"','LOGO' : ''}")
    
    conf.close()

    def __init__(self, s):
        self.configuration = eval(s)

    def set_configuration(self):
        self.SERVER = self.configuration['SERVER']
        self.HOST = self.configuration['HOST']
        self.DATABASE = self.configuration['DATABASE']
        self.PASSWORD = self.configuration['PASSWORD']
        self.PORT = self.configuration['PORT']
        self.USER = self.configuration['USER']
        self.THUMB_PATH = self.configuration['THUMB_PATH']
        self.THUMB_RESIZE = self.configuration['THUMB_RESIZE']
        self.SITE_SET = self.configuration['SITE_SET']
        self.LOGO = self.configuration['LOGO']
        PLUGIN_PATH = path = os.path.dirname(__file__)
