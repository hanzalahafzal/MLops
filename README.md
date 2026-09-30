# Production Text Summarization Service

[![Python MLOps CI](https://github.com/hanzalahafzal/MLops/actions/workflows/main.yml/badge.svg)](https://github.com/hanzalahafzal/MLops/actions/workflows/main.yml)

An abstractive text summarization web application built with Hugging Face Transformers (`sshleifer/distilbart-cnn-12-6`) and Gradio, fully integrated with GitHub Actions CI/CD.

## 🚀 Live Demo
Access the running application interface here:
- **Live UI**: [Text Summarizer Service](https://legendary-space-meme-r47jwj4vqqxpcx954-7860.app.github.dev/)

*(Note: The link is active whenever the application process is running inside GitHub Codespaces).*

---

## 🛠️ Project Structure
- `app.py`: Gradio web interface and inference pipeline logic.
- `test_app.py`: Fast unit test suite with pipeline mocking for CI.
- `Makefile`: Automated routines for setup (`install`), code quality (`lint`, `format`), and testing (`test`).
- `.github/workflows/main.yml`: Automated GitHub Actions pipeline for continuous integration.
- `requirements.txt`: Pinned Python dependencies.

---

## 💻 Local Setup & Execution

1. **Install dependencies:**
   ```bash
   make install