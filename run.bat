@echo off

start cmd /k python main.py
start cmd /k "cd /d music_addon\data\lavalink && java -jar lavalink.jar"

pause
