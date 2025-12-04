==================================
Port Scanner

A lightweight Python-based TCP port scanner with a minimal Streamlit front-end. This project provides a simple interface for checking open ports on a target host and includes a basic prototype scanner script using Python’s socket module.

Status: Prototype. The current UI and scanner logic are functional but minimal, and may require further expansion depending on the use case.

Features

– Streamlit UI to enter hostnames/IP addresses and scan single ports or ranges
– Basic socket-based TCP port scanning
– Option to run either through the web app or directly via the scanner script

Live Demo

A hosted version is available at:
https://aphrodite1818-port-scanner.streamlit.app/

Note: Hosted environments cannot access private/local network addresses such as localhost, 127.0.0.1, or 192.168.x.x. To scan local networks or your own machine, run the app locally.

Project Structure

Port_Scanner_App/
│ app.py (Streamlit app entry point)
│ port_scanner.py (core scanner logic)
requirements.txt

Prerequisites

– Python 3.8+
– (Recommended) A virtual environment for dependency isolation

Setup (Windows / PowerShell)

Navigate to the project folder:

cd Port_scanner

(Optional) Create and activate a virtual environment:

python -m venv .venv
..venv\Scripts\Activate.ps1

Install dependencies:

pip install -r requirements.txt

Running the App (Streamlit UI)

From the project root, run:

streamlit run Port_Scanner_App/app.py

Streamlit will launch the web interface in your browser (typically http://localhost:8501
).

Running the Scanner Directly

You can run the underlying scanner script without the UI:

python Port_Scanner_App/port_scanner.py

Troubleshooting

– If Streamlit does not run, ensure it is installed in the active environment.
– If the script cannot import modules, confirm your virtual environment is active.
– File paths may differ depending on your OS; adjust as needed.

Usage & Legal Notice

This tool is intended strictly for learning, testing, and security assessment on networks and systems you have permission to scan. Unauthorized port scanning may violate laws or service agreements. The author is not responsible for misuse or consequences arising from the use of this software.

==================================