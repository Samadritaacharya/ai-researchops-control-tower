Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

Write-Host 'AI ResearchOps Control Tower - Windows launcher'

if (-not (Test-Path 'requirements.txt')) {
    Write-Host 'requirements.txt not found. Please run this script from inside the ai-researchops-control-tower folder.' -ForegroundColor Red
    exit 1
}

if (-not (Test-Path '.venv')) {
    Write-Host 'Creating virtual environment...'
    py -m venv .venv
}

Write-Host 'Activating virtual environment...'
. .\.venv\Scripts\Activate.ps1

Write-Host 'Installing dependencies...'
py -m pip install --upgrade pip
py -m pip install -r requirements.txt

Write-Host 'Running tests...'
py -m pytest tests

Write-Host 'Starting Streamlit app...'
py -m streamlit run app.py
