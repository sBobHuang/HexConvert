#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from datetime import timedelta

from flask import Flask
from flask_bootstrap import Bootstrap, WebCDN, ConditionalCDN, BOOTSTRAP_VERSION, \
    JQUERY_VERSION, HTML5SHIV_VERSION, RESPONDJS_VERSION
from config import config

bootstrap = Bootstrap()



def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)
    # 使用默认的flask配置
    bootstrap.init_app(app)
    change_cdn_domestic(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    # 倒入蓝图

    return app


def change_cdn_domestic(tar_app):
    static = tar_app.extensions['bootstrap']['cdns']['static']
    local = tar_app.extensions['bootstrap']['cdns']['local']

    def change_one(tar_lib, tar_ver, fallback):
        tar_lib_new = "twitter-bootstrap" if tar_lib == "bootstrap" else tar_lib
        tar_js = ConditionalCDN('BOOTSTRAP_SERVE_LOCAL', fallback,
                                WebCDN('//cdn.staticfile.org/' + tar_lib_new + '/' + tar_ver + '/'))
        tar_app.extensions['bootstrap']['cdns'][tar_lib] = tar_js

    libs = {'jquery': {'ver': JQUERY_VERSION, 'fallback': local},
            'bootstrap': {'ver': BOOTSTRAP_VERSION, 'fallback': local},
            'html5shiv': {'ver': HTML5SHIV_VERSION, 'fallback': static},
            'respond.js': {'ver': RESPONDJS_VERSION, 'fallback': static}}
    for lib, par in libs.items():
        change_one(lib, par['ver'], par['fallback'])
