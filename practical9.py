"""
Practical 9: Deployment of AI Agent Application
Deployment Verification & Automation Script
"""

import os
import sys
import subprocess
import shutil

def verify_deployment_readiness():
    print("=" * 65)
    print("                      PRACTICAL 9")
    print("          Deployment of AI Agent Application")
    print("=" * 65)
    print("\n[1/5] Checking Cloud Deployment Prerequisites...")

    # Required files for cloud deployment
    required_files = [
        "app.py",
        "requirements.txt",
        ".gitignore",
        "README.md",
        ".streamlit/config.toml"
    ]

    all_files_present = True
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    for filename in required_files:
        filepath = os.path.join(base_dir, filename)
        if os.path.exists(filepath):
            print(f"  [OK] Found required file: {filename}")
        else:
            print(f"  [MISSING] Missing required file: {filename}")
            all_files_present = False

    # Check Git installation
    print("\n[2/5] Checking Version Control Tool (Git)...")
    git_path = shutil.which("git")
    if git_path:
        try:
            git_ver = subprocess.check_output(["git", "--version"], text=True).strip()
            print(f"  [OK] Git is installed and available: {git_ver}")
        except Exception:
            print("  [!] Git executable found, but version check had an issue.")
    else:
        print("  [!] Git not found in PATH.")

    # Check Python environment & libraries
    print("\n[3/5] Checking Cloud Deployment Dependencies...")
    for lib in ["streamlit", "dotenv", "requests"]:
        try:
            __import__(lib)
            print(f"  [OK] Library '{lib}' is installed.")
        except ImportError:
            print(f"  [X] Library '{lib}' is NOT installed.")

    # Cloud deployment instructions
    print("\n[4/5] Streamlit Community Cloud Deployment Steps:")
    print("  Step 1: Initialize Git and stage files:")
    print("          git init")
    print("          git add .")
    print('          git commit -m "Initial Commit - Deploy AI Agent"')
    print("  Step 2: Push repository to GitHub:")
    print("          git branch -M main")
    print("          git remote add origin https://github.com/<your-username>/<repo-name>.git")
    print("          git push -u origin main")
    print("  Step 3: Connect to Streamlit Community Cloud:")
    print("          Go to https://share.streamlit.io")
    print("          Click 'New app', select the GitHub repository, branch 'main', and entry point 'app.py'")
    print("  Step 4: Deploy & Access:")
    print("          Click 'Deploy!'")
    print("          Live URL will be generated: https://<your-app>.streamlit.app")

    # Local testing command
    print("\n[5/5] Local Testing Command:")
    print("  streamlit run app.py")
    print("=" * 65)

    if all_files_present:
        print("\nSUCCESS: All deployment configuration files are ready for publishing!")
    else:
        print("\nWARNING: Please ensure all required files are generated before deploying.")

if __name__ == "__main__":
    verify_deployment_readiness()
