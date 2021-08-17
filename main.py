#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import speedtest
from flask import Flask
from flask import jsonify
from flask_httpauth import HTTPBasicAuth
from gevent import pywsgi


def main():
    USERNAME = sys.argv[1]
    PASSWORD = sys.argv[2]

    app = Flask(__name__)
    auth = HTTPBasicAuth()

    @app.route('/', methods=['GET'])
    @auth.login_required
    def start():
        s = speedtest.Speedtest()
        s.get_best_server()
        s.download()
        s.upload()
        s.results.share()
        results_dict = s.results.dict()

        download = "{:.2f} Mbps".format(results_dict["download"] / 1e6)
        upload = "{:.2f} Mbps".format(results_dict["upload"] / 1e6)
        ping = "{:.0f} ms".format(results_dict["ping"])

        return jsonify({"img": results_dict["share"],
                        "download": download,
                        "upload": upload,
                        "ping": ping
                        })

    @auth.get_password
    def get_password(username):
        if username == USERNAME:
            return PASSWORD
        return None

    server = pywsgi.WSGIServer(('0.0.0.0', 8000), app)
    server.serve_forever()


if __name__ == '__main__':
    main()
