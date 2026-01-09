"""
Launcher script for the Streamlit dashboard
Run this file directly in DataSpell
"""
import os
import sys

# Add streamlit to the path
os.chdir('C:/Users/me25l/OneDrive - Florida State University/8K reaction')

# Run streamlit
from streamlit.web import cli as stcli

if __name__ == '__main__':
    sys.argv = ["streamlit", "run", "Dashboard.py"]
    sys.exit(stcli.main())
