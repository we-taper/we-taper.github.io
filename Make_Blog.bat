@echo off
cd pelican
pelican content
cd ..
python -m http.server
