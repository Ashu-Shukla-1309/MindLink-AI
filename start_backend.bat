@echo off
cd /d "%~dp0backend"
echo ==== Starting backend in %cd% ====
python -m uvicorn app:app --host 127.0.0.1 --port 8000 --reload
echo ==== Backend exited ====
pause
