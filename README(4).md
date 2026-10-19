# CrewAI Multiple Agents

A Streamlit web application demonstrating a multi-agent AI workflow powered by CrewAI.

## 🚀 Live Demo

Try the deployed application here:

**[CrewAI Multiple Agents — Live App](https://crewaimultipleagents-jwemp6kmamdzbxbedkerzm.streamlit.app/)**

## 📌 Overview

This project provides a web interface for exploring a multi-agent AI workflow. Multiple specialized AI agents can collaborate on a task, with each agent contributing according to its configured role and goal.

> Note: The exact agent roles, model provider, inputs, and outputs depend on the implementation and configuration in this project's source code.

## ✨ Features

- **Interactive web interface:** Access the app through Streamlit.
- **Multi-agent workflow:** Organize work among specialized AI agents.
- **Collaborative task execution:** Agents can contribute different perspectives to a task.
- **Cloud deployment:** The application is available online through Streamlit Community Cloud.

## 🧰 Technologies

- **Python** — application logic
- **Streamlit** — web interface and deployment
- **CrewAI** — multi-agent orchestration

Additional packages and model providers may be used depending on the source code and `requirements.txt`.

## 🖥️ Run Locally

### 1. Clone your GitHub repository

Replace `<YOUR_GITHUB_REPOSITORY_URL>` with your repository's clone URL:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd <YOUR_PROJECT_FOLDER>
```

### 2. Create and activate a virtual environment

**Linux / macOS**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows**
```powershell
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

If your project contains a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

If it does not, install the packages required by your source code. For a basic Streamlit + CrewAI project:

```bash
pip install streamlit crewai
```

Use the project's actual dependency versions when available.

### 4. Configure environment variables

If the application uses an API key or other secrets, create a `.env` file (if the code loads it) or configure the variables in your shell / Streamlit secrets.

Example only:

```env
# Add only the variables required by your application.
# MODEL_PROVIDER_API_KEY=your_api_key_here
```

**Security:** Never commit API keys, passwords, or private credentials to GitHub. Add `.env` to `.gitignore` and use Streamlit Community Cloud's app secrets for deployed secrets.

### 5. Start the application

Run the command from the project folder:

```bash
streamlit run app.py
```

If your Streamlit entry-point file has a different name, replace `app.py` with that filename. Open the local URL shown in the terminal, usually `http://localhost:8501`.

## ☁️ Deployment

This project is deployed on Streamlit Community Cloud.

Live URL: https://crewaimultipleagents-jwemp6kmamdzbxbedkerzm.streamlit.app/

To deploy your own copy:
1. Push the project to a GitHub repository.
2. Open [Streamlit Community Cloud](https://share.streamlit.io/).
3. Create a new app and select the repository, branch, and Streamlit entry-point file.
4. Add any required secrets under the app's settings.
5. Deploy and check the app logs if startup fails.

## 📂 Suggested Repository Structure

Your actual files may differ. A typical project may look like this:

```text
project/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── .streamlit/
    └── secrets.toml   # Keep secrets out of GitHub
```

## 🛠️ Troubleshooting

- **App is stuck loading or shows an error:** Open the Streamlit app dashboard and check the logs.
- **Module not found:** Confirm the package is listed in `requirements.txt` and redeploy.
- **Missing API key:** Add the required key in Streamlit app secrets, using the exact variable name expected by your code.
- **Works locally but not in the cloud:** Check Python/package compatibility and confirm the entry-point file and secrets are configured correctly.

## 🔒 Security

- Do not upload `.env`, `secrets.toml`, API keys, or credentials to a public repository.
- Use `.gitignore` to exclude local secrets and virtual environments.
- Only describe features and agent roles that are implemented in the source code.

## 📄 License

No license information was provided. Add a `LICENSE` file if you intend to distribute this project and choose a license appropriate for your needs.

## 👩‍💻 Author

CHANDRIKA T
https://github.com/chandrika434
