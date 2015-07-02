@echo OFF

CD %PYTHONPATH%\test_case\desktop_v3\_flow
START python test_help.py
START python test_login.py

PAUSE