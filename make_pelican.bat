echo off
cd pelican
pelican content -s pelicanconf.py
cd ..
python -m SimpleHTTPServer
