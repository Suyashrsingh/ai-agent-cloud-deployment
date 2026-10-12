Practical 9 – Deployment Of AI Agent Application

Aim

To deploy an AI Agent application on a cloud platform for online accessibility.

------------------------Objectives-------------------------------------

1. Understand the principles and architecture of cloud application deployment.
2. Configure cloud deployment files (`requirements.txt`, `.gitignore`, `.streamlit/config.toml`, `app.py`).
3. Set up version control using Git and publish code to GitHub.
4. Publish and host the Streamlit application on Streamlit Community Cloud.
5. Access, test, and verify the AI Agent online via a public URL.

------------------------Software Requirements-------------------------------

- Python 3.10+
- Streamlit
- Git Version Control System
- GitHub Account
- Streamlit Community Cloud (or Hugging Face Spaces / Render)
- Web Browser

--------------------Libraries Used----------------------------

- Streamlit
- python-dotenv
- requests

--------------------Theory----------------------------------------

Deployment is the process of transferring, configuring, and publishing software applications to internet-accessible servers so that end users worldwide can interact with them through web browsers or APIs.

Popular cloud platforms for AI Agent applications:
- Streamlit Community Cloud (Fastest serverless hosting for Streamlit Python apps)
- Hugging Face Spaces (Ideal for ML / AI demo hosting)
- Render (PaaS for web apps and backend services)
- Railway / Heroku
- Microsoft Azure / AWS Cloud (Enterprise containerized deployments)

Deployment Steps:
1. Create a GitHub repository and commit all application code.
2. Ensure dependency management with `requirements.txt`.
3. Connect GitHub account with Streamlit Community Cloud.
4. Select the repository, branch (`main`), and target file (`app.py`).
5. Configure cloud secrets (`st.secrets`) for API keys.
6. Deploy application and test generated public URL.

Advantages of Cloud Deployment:
- Global 24/7 Accessibility: Anyone with an internet connection can use the AI Agent.
- Continuous Integration & Deployment (CI/CD): Pushing updates to the GitHub repository automatically updates the live cloud app.
- Scalability & Resource Offloading: Computation is performed on cloud infrastructure rather than relying on local machine resources.
- Centralized Secret Management: Sensitive API credentials remain securely masked in cloud vault settings.

--------------------Algorithm-----------------------------------

1. Start.
2. Create and initialize a Git repository.
3. Upload project files to GitHub.
4. Login to Streamlit Community Cloud (`share.streamlit.io`).
5. Connect GitHub repository and select the app branch and main file `app.py`.
6. Add environment secrets in cloud settings.
7. Click Deploy to build and publish the application.
8. Verify the deployment using the generated web URL.
9. Share application URL.
10. Stop.

--------------------Flowchart-----------------------------------

        Start
          │
  Create Repository
          │
    Upload Files
          │
Connect Streamlit Cloud
          │
  Deploy Application
          │
    Generate URL
          │
  Test Application
          │
        Stop

--------------------Deployment Commands-------------------------

Local Git Preparation:
   git init
   git add .
   git commit -m "Initial Commit"
   git branch -M main
   git remote add origin https://github.com/<your-username>/<repo-name>.git
   git push -u origin main

Local Testing:
   streamlit run app.py
   (or: python practical9.py)

--------------------Expected Output-----------------------------

Deployment Verification:
   All deployment configuration files are ready for publishing!
   Git is installed and available.

Local Execution:
   Local URL: http://localhost:8501
   Network URL: http://192.168.x.x:8501

Cloud Deployed Output:
   Application deployed successfully
   URL: https://your-app.streamlit.app

----------------------Assessment / Viva Questions & Answers------

1. What is GitHub?
   Ans: GitHub is a cloud-based hosting platform for software development and version control using Git. It allows developers to store code, track revision history, collaborate with teams, and trigger automated deployment workflows.

2. What is Streamlit Cloud?
   Ans: Streamlit Community Cloud is an open-source platform that enables developers to deploy, manage, and share Streamlit Python web applications directly from their GitHub repositories without needing server configuration or DevOps overhead.

3. What is cloud computing?
   Ans: Cloud computing is the on-demand delivery of computing services—including servers, storage, databases, networking, software, and intelligence—over the Internet ("the cloud") offering flexible resources, economies of scale, and global accessibility.

4. What is a repository?
   Ans: A repository (or "repo") is a storage location where all project files, directories, historical revisions, commit logs, and documentation for a software project are organized and managed by a version control system like Git.

----------------------Result--------------------------------------

The AI Agent application was successfully packaged with cloud configuration, verified for deployment prerequisites, and prepared for cloud publishing on Streamlit Community Cloud with a live web URL.
