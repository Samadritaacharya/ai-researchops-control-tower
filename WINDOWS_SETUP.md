# Windows PowerShell Setup

Your PowerShell must be inside the project folder before running install, tests, or Streamlit.

## Fresh setup

Open PowerShell and run:

```powershell
cd $HOME
git clone https://github.com/Samadritaacharya/ai-researchops-control-tower.git
cd ai-researchops-control-tower
py -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
py -m pip install --upgrade pip
py -m pip install -r requirements.txt
py -m pytest tests
py -m streamlit run app.py
```

## If the repo is already downloaded

```powershell
cd $HOME\ai-researchops-control-tower
.\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
py -m pytest tests
py -m streamlit run app.py
```

## Why `python -m` / `py -m` is used

On Windows, commands like `pytest` or `streamlit` may not be recognized even after installation if the Scripts folder is not on PATH. Running them as Python modules avoids that problem:

```powershell
py -m pytest tests
py -m streamlit run app.py
```

## Common error

If you see:

```text
Could not open requirements file: No such file or directory: requirements.txt
```

You are not inside the project folder. Run:

```powershell
cd $HOME\ai-researchops-control-tower
```

Then try again.
