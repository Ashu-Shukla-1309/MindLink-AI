@echo off
setlocal

REM Launch backend and frontend helper scripts each in their own window
start "MindLink Backend" "%~dp0start_backend.bat"
start "MindLink Frontend" "%~dp0start_frontend.bat"

REM Give them a moment then open the browser
timeout /t 3 /nobreak >nul
start "" "http://localhost:5173"

echo Launched. Check the Backend and Frontend windows for logs.
pause
endlocal
