# -*- coding: utf-8 -*-
from distutils.core import setup
from distutils.extension import Extension
import os
import subprocess

setup(  name             = "n4d-moving-profiles",
        version          = "2.5",
        author           = "Enrique Medina Gremaldos",
        author_email     = "quiqueiii@gmail.com",
        url              = "https://github.com/lliurex/n4d-moving-profiles",
        data_files  =   [("/usr/share/n4d/python-plugins/",["MovingProfiles.py"]),
                        ("/etc/moving-profiles/",["setup.conf"]),
                        ("/etc/n4d/conf.d/",["MovingProfiles.json"])
                        ]
        
     )
