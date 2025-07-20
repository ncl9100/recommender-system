@echo off
echo Starting Recommender System...
echo.

echo Starting Backend Server...
start "Backend" cmd /k "cd backend && python -m venv venv && venv\Scripts\activate && pip install -r requirements.txt && uvicorn app.main:app --reload"

echo.
echo Starting Frontend Server...
start "Frontend" cmd /k "cd frontend && npm install && npm run dev"

echo.
echo Servers are starting...
echo Backend will be available at: http://localhost:8000
echo Frontend will be available at: http://localhost:5173
echo.
echo Press any key to exit...
pause > nul 