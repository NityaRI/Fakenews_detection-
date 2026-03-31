# Start Fake News Detection App

Write-Host "Starting Backend (FastAPI)..." -ForegroundColor Green
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd backend; python -m uvicorn main:app --reload --port 8000"

Write-Host "Starting Frontend (Vite)..." -ForegroundColor Cyan
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd frontend; npm run dev"

Write-Host "-------------------------------------------"
Write-Host "Backend running at: http://localhost:8000"
Write-Host "Frontend running at: http://localhost:3000"
Write-Host "-------------------------------------------"
Write-Host "Press Ctrl+C to stop this script (though processes will remain open in new windows)."
