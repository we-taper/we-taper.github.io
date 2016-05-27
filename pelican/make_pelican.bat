echo off
pelican content -s pelicanconf.py
cd ..
python -m SimpleHTTPServer
