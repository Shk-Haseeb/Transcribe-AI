# 🧠 Transcribe-AI

**Transcribe-AI** is a GenAI-powered assistant that transcribes, summarizes, and simplifies meeting or lecture audio — so no one falls behind.

🎯 **Built with real-world users in mind**, based on interviews with professionals who struggle to catch up after missed meetings.

[![Streamlit App](https://img.shields.io/badge/Live%20App-Streamlit-success?style=flat&logo=streamlit)](https://transcribe-ai-demo.streamlit.app/)  
📽️ [Watch our original concept demo video](data/ELISA-AI-DEMO.mp4)

---

## What It Does

- 🔊 Upload audio from meetings or lectures
- 📃 Transcribes speech to text (via AssemblyAI)
- ✍️ Summarizes key points (via Hugging Face Transformers)
- 🪄 Simplifies language for easy reading
- 📥 Export as `.txt` or `.pdf`

---


## Why We Built It

Modern teams and students rely heavily on virtual meetings and recorded lectures. But when someone misses a session due to scheduling conflicts, timezone differences, or emergencies, catching up becomes difficult and inefficient.

During the Elisa AI Hackathon, we interviewed professionals across different industries. One insight came up repeatedly:

> “I miss one meeting, and I spend half a day trying to catch up.”

This pain point inspired Transcribe-AI.

We designed and built this tool to make missed content instantly accessible. Instead of replaying entire recordings or relying on someone else's notes, users can upload audio and get clean transcriptions, concise summaries, and simplified notes—all in minutes.

Transcribe-AI helps people stay informed, make better decisions faster, and eliminate the frustration of information overload.


---

## AI/ML Tools Used

| Task | Tool |
|------|------|
| Audio Transcription | AssemblyAI |
| Summarization & Simplification | Hugging Face `facebook/bart-large-cnn` |
| Prompt-based rewriting | Custom instructions |
| Optional GPT Support | Swappable OpenAI API (archived) |

---

## 🔥 Screenshots / Demo
