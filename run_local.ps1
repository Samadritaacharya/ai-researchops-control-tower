Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

Write-Host 'AI ResearchOps Control Tower - Windows launcher'

if (-not (Test-Path 'requirements.txt')) {
    Write-Host 'requirements.txt not found. Run this script from inside the ai-researchops-control-tower folder.' -ForegroundColor Red
    Write-Host 'Example: cd C:\Users\HP\Downloads\ai-researchops-control-tower'
    exit 1
}

function Get-PreferredPython {
    $candidates = @('3.11', '3.12', '3.13')
    foreach ($v in $candidates) {
        try {
            py -$v -c "import sys; print(sys.version)" | Out-Null
            return "py -$v"
        } catch {}
    }
    Write-Host 'Python 3.11/3.12/3.13 was not found. Falling back to default py. If install fails, install Python 3.11 from python.org.' -ForegroundColor Yellow
    return 'py'
}

$PY = Get-PreferredPython
Write-Host "Using Python command: $PY"

if (-not (Test-Path '.venv')) {
    Write-Host 'Creating virtual environment...'
    Invoke-Expression "$PY -m venv .venv"
}

Write-Host 'Activating virtual environment...'
. .\.venv\Scripts\Activate.ps1

Write-Host 'Installing dependencies...'
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

Write-Host 'Running tests...'
python -m pytest tests

Write-Host 'Starting Streamlit app...'
python -m streamlit run app.py
