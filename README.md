# 🌸 Waguri AI - Interactive Portfolio Assistant

An intelligent, voice-enabled virtual assistant designed to transform a static portfolio into an interactive two-way conversation. Built with modern Retrieval-Augmented Generation (RAG) architecture and Strict AI Safety Guardrails.

## 🎯 Project Overview
Traditional CVs and PDF portfolios are static and often fail to answer specific questions recruiters might have. **Waguri AI** solves this by acting as a personal PR agent. Recruiters and visitors can chat directly with Waguri to explore my engineering skills, academic projects, and professional goals in real-time.

## ✨ Key Features
- **Conversational RAG:** Accurately answers questions based on my provided portfolio document without hallucinating.
- **Modern LCEL Architecture:** Built using LangChain Expression Language (LCEL) for a transparent, fast, and stable data pipeline.
- **Strict Security Guardrails:** Engineered with robust prompt constraints to prevent Prompt Injection attacks (e.g., users cannot trick the AI into generating random code or ignoring its core directive).
- **Voice Accessibility:** Integrated with Google Text-to-Speech (gTTS) allowing users to listen to the AI's responses.
- **Responsive UI:** Clean and intuitive chat interface built with Streamlit.

## 🛠️ Technology Stack
- **Frontend:** Streamlit, HTML5/CSS3 (Markdown)
- **Core AI Logic:** LangChain (LCEL `langchain_core`)
- **LLM Engine:** Llama 3.3 (via Groq API) for high-speed inference
- **Embeddings & Vector Store:** HuggingFace (`sentence-transformers/all-MiniLM-L6-v2`) & FAISS (CPU)
- **Audio Processing:** gTTS (Google Text-to-Speech) & `io.BytesIO`

## 🚀 How to Run Locally

### 1. Clone the Repository
```bash
git clone [[https://github.com/yourusername/waguri-ai.git](https://github.com/Pacartopaz/waguri-ai.git)]
cd waguri-ai