@echo off
cd /d "%~dp0frontend"
echo ==== Starting frontend in %cd% ====

REM If node_modules missing, run install (fast if already present)
if not exist node_modules (
  echo node_modules missing — running npm install...
  npm install --no-audit --no-fund
) else (
  echo node_modules exists — skipping install
)

REM Ensure vite present (safe noop if already installed)
npm ls vite --depth=0 >nul 2>&1 || npm install --no-audit --no-fund --save-dev vite@^5.0.0

echo Launching Vite (local)...
npm exec -- vite -- --port 5173 --host 127.0.0.1

echo ==== Frontend exited ====
pause
