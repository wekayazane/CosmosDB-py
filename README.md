# CosmosDB-py — venv & run instructions

This project contains `app.py` which uses `azure.cosmos`.

Quick steps (PowerShell):

1. Create the virtual environment (from project root):

```powershell
py -3 -m venv .venv
```

2. Activate the venv in PowerShell:

```powershell
# Dot-source the activation script
. .\.venv\Scripts\Activate.ps1
```

If you get an execution policy error, allow local script execution for the current user:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
# Then activate again
. .\.venv\Scripts\Activate.ps1
```

3. Install dependencies and run the app:

```powershell
python -m pip install --upgrade pip
python -m pip install -r .\requirements.txt
python app.py
```

Other shells:

- Command Prompt (cmd.exe):

```cmd
.\.venv\Scripts\activate.bat
```

- Git Bash on Windows (may need to use MSYS path):

```bash
source .venv/Scripts/activate
```

- WSL / Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

To leave the venv in any shell: `deactivate`.

Notes:
- The example `app.py` connects to a local Cosmos DB emulator — ensure the emulator is running (or change connection info) before running `app.py`.
- If `py` or `python` are not found, install Python or use the absolute path to `python.exe`.
