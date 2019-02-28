# -*- coding: utf-8 -*-
from distutils.core import setup
from distutils.extension import Extension
import os
import subprocess



setup(  name             = "n4d-moving-profiles",
        version          = "2.0",
        author           = "Enrique Medina Gremaldos",
        author_email     = "quiqueiii@gmail.com",
        url              = "http://lliurex.net/home/",
        data_files  =   [("/usr/share/n4d/python-plugins/",["install/usr/share/n4d/python-plugins/MovingProfiles.py"]),
                        ("/usr/share/n4d-moving-profiles/",["install/usr/share/n4d-moving-profiles/setup.conf"]),
                        ("/etc/n4d/conf.d/",["install/etc/n4d/conf.d/MovingProfiles"])
                        ]
        
     )

