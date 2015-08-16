#!/bin/sh

yum install -y epel-release
yum install -y nginx python-pip python-virtualenv python-virtualenvwrapper
pip install flask
pip install Flask-WTF
pip install Flask-SQLAlchemy
