# Step-by-Step Guide: Deploying Your AI Agent to Streamlit Community Cloud

This guide explains how to deploy the AI Agent developed in **Practical 9** to the web using **GitHub** and **Streamlit Community Cloud**.

---

## Prerequisites
1. A free [GitHub Account](https://github.com)
2. A free [Streamlit Community Cloud Account](https://share.streamlit.io) (sign in with your GitHub account)
3. Git installed on your computer

---

## Step 1: Initialize Git and Prepare Files

Open terminal in the `Practical_9_Deployment` folder and run:

```bash
# 1. Initialize local git repository
git init

# 2. Stage all files (respecting .gitignore)
git add .

# 3. Create initial commit
git commit -m "Deploy AI Agent to Cloud"
```

---

## Step 2: Push to GitHub

1. Go to [GitHub](https://github.com) and click **New Repository**.
2. Name it `ai-agent-cloud` (or any preferred name). Keep it **Public**.
3. Do NOT initialize with README or .gitignore (we already created them).
4. Run the commands shown by GitHub:

```bash
git branch -M main
git remote add origin https://github.com/<YOUR_GITHUB_USERNAME>/ai-agent-cloud.git
git push -u origin main
```

---

## Step 3: Connect and Deploy on Streamlit Community Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io/) and log in with your GitHub account.
2. Click **Create app** (or **New app**).
3. Fill in the repository details:
   - **Repository:** `Suyashrsingh/ai-agent-cloud-deployment`
   - **Branch:** `main`
   - **Main file path:** `app.py`
   - **App URL (custom):** `ai-agent-suyash.streamlit.app` (or any available name)
4. Configure Secrets (API Keys):
   - Click **Advanced settings...**
   - In the **Secrets** section, paste:
     ```toml
     ATRIA_API_KEY = "atr_n7FB_XvmYAJ0P4cDFL1b46Ix7P-8w3_B"
     ```
   - Click **Save**.
5. Click **Deploy!**

---

## Step 4: Verify Live Application

- Streamlit Cloud will install dependencies from `requirements.txt` and launch the app.
- Once finished, your application will be live at:
  ```
  https://<your-app-name>.streamlit.app
  ```
- Test sending queries (e.g. `Explain Machine Learning`, `What is Cloud Deployment?`) to verify live generation.
