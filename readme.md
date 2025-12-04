
# Port Scanner

A small Python port-scanning project with a minimal Streamlit front-end and a simple scanner script. This repository contains a prototype for discovering open TCP ports on a target host.

**Status:** Prototype — basic files present. The Streamlit app and scanner script are minimal and may need further implementation to add a full UI and scanning features.

**Contents:**
- `Port_Scanner_App/app.py` — (Streamlit app entry, currently minimal)
- `Port_Scanner_App/port_scanner.py` — simple Python script using `socket` (prototype)
- `requirements.txt` — Python dependencies

**What this project does (basics):**
- Intends to provide a small UI (Streamlit) where you can enter a hostname/IP and a port or port range, then scan for open TCP ports.
- Includes a very small prototype scanner script that demonstrates creating sockets and attempting connections.

**Try it Online**

An online version is available here: **[https://aphrodite1818-port-scanner.streamlit.app/](https://aphrodite1818-port-scanner.streamlit.app/)**

⚠️ **Important:** The online version can only scan targets that are publicly accessible (online services, external hosts). It **cannot** scan your local machine or private network addresses (`localhost`, `127.0.0.1`, `192.168.x.x`, etc.) due to network restrictions of the hosting environment.

For scanning your local machine or private network, you must run the app locally (see setup below).

**Prerequisites**
- Python 3.8+ installed (adjust if using a different interpreter)
- (Recommended) Use a virtual environment to avoid polluting the global Python environment.

**Quick setup (Windows PowerShell)**

1. Open PowerShell and navigate to the project folder:

```
cd Port_scanner
```

2. (Optional) If you want to create a fresh virtual environment:

```
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. If you prefer to use the included `scanner` virtual environment, activate it instead:

```
.\scanner\Scripts\Activate.ps1
```

4. Install dependencies:

```
pip install -r requirements.txt
```

**Run the Streamlit app**

Start the UI with Streamlit (from the project root):

```
streamlit run Port_Scanner_App/app.py
```

This will open a local web UI (usually at `http://localhost:8501`) where the app can prompt for input. Note: the current `app.py` is a minimal placeholder — if it is empty you may need to add UI code or run the script directly (see below).

**Run the scanner script directly**

You can run the prototype scanner script (it's minimal and may not provide interactive prompts):

```
python Port_Scanner_App/port_scannner.py
```

**Troubleshooting**
- If Streamlit fails to start, ensure it is installed in the active environment (`pip install streamlit`).

**Usage & Disclaimer**

- This tool is provided for educational and testing purposes only. Use it responsibly and only scan systems and networks for which you have explicit permission.
- The author is not responsible or liable for any misuse, damage, loss, or legal consequences resulting from the use of this software.
- By using this tool you agree to follow applicable laws and your organization or provider's acceptable use policies.