# LangGraph🦜🕸️ – Develop LLM-Powered AI Agents


![Logo](https://github.com/emarco177/langgraph-course/blob/main/banner.png)

[![Udemy](https://img.shields.io/badge/Udemy-Course-EC5252?style=for-the-badge&logo=udemy&logoColor=white)](https://www.udemy.com/course/langgraph/?couponCode=APRIL-2025) 
[![Rating](https://img.shields.io/badge/Rating-4.7/5-brightgreen?style=for-the-badge)](https://www.udemy.com/course/langgraph/) 
[![Students](https://img.shields.io/badge/Students-13K+-blue?style=for-the-badge)](https://www.udemy.com/course/langgraph/?couponCode=APRIL-2025)
[![Twitter](https://img.shields.io/twitter/follow/EdenEmarco177?label=Follow&style=social)](https://twitter.com/EdenEmarco177)

> **Build production-grade AI agents—fast.** This repository is the hands-on companion to my Udemy bestseller. Every branch is a *project*, every commit is a *lesson*. Clone it, code along, and ship your own LangGraph agents.

---

## 🚀  What You'll Build

- **Agentic RAG** – Retrieval-Augmented Generation with self-correction & adaptive routing  
- **ReAct Agent** – Reasoning + Acting loop implemented in LangGraph  
- **Reflection & Reflexion Agents** – Agents that critique and improve themselves  
- **Multi-Step Graphs** – Complex flows with conditionals, parallelism, and web-search tools

---

## 🗂️  Repository Map

| Branch | Project Snapshot | Live Code |
|--------|------------------|-----------|
| **project/agentic-rag** | Advanced RAG pipeline with grading, web-search & adaptive routing | [link](https://github.com/emarco177/langgaph-course/tree/project/agentic-rag) |
| **project/ReAct-agent** | Classic ReAct (Reason + Act) agent in LangGraph | [link](https://github.com/emarco177/langgaph-course/tree/project/ReAct-agent) |
| **project/reflection** | Minimal reflection demo – the *why* before the *wow* | [link](https://github.com/emarco177/langgaph-course/tree/project/reflection) |
| **project/reflection-agent** | Full reflection agent that revises its own output | [link](https://github.com/emarco177/langgaph-course/tree/project/reflection-agent) |
| **project/reflexion-agent** | Reflexion agent that learns from past runs | [link](https://github.com/emarco177/langgaph-course/tree/project/reflexion-agent) |

> ✨ **Tip:** Checkout a branch, then use `git log --oneline` to watch the lessons unfold commit-by-commit.

---

## 📚  Lesson-By-Lesson: *Agentic RAG* Branch

| # | Commit | Lesson Title | Key Skill |
|---|--------|--------------|-----------|
| 1 | `5b2b18e` | Project Kick-Off | Repo & env setup |
| 2 | `2693185` | Folder Structure 101 | Clean project scaffolding |
| 3 | `513e3cf` | Ingestion Pipeline | Load & embed data |
| 4 | `03f79ae` | Graph State | Passing memory between nodes |
| 5 | `c2d71c7` | Retrieve Node | Context fetching with LangGraph |
| 6 | `9107e7a` | Grade Docs Node | Structured relevance filtering |
| 7 | `6d4fdc4` | Web Search Node | Tavily API integration |
| 8 | `bc57b63` | Generation Node | Prompting & LLM calls |
| 9 | `a450f9b` | Wiring the Graph | Fan-in, fan-out, conditionals |
| 10 | `5400fb7` | Self-RAG | Let the LLM critique itself |
| 11 | `034e53f` | Adaptive Router | Dynamic tool selection |

Feel free to cherry-pick commits or rewind with `git checkout <hash>` to experiment.

---

## ⚡  Quick Start

```bash
# 1. Clone & enter
$ git clone https://github.com/emarco177/langgaph-course.git
$ cd langgaph-course

# 2. Choose a project branch
$ git checkout project/agentic-rag  # for example

# 3. Install deps (Poetry)
$ poetry install

# 4. Run
$ poetry run python main.py
```

Create a `.env` file:

```bash
OPENAI_API_KEY=...
TAVILY_API_KEY=...          # optional – for web-search lessons
LANGCHAIN_API_KEY=...       # optional – for LangSmith tracing
LANGCHAIN_TRACING_V2=true   # optional
PYTHONPATH=$(pwd)
```

---

## 💼  Level-Up Your Career: LangJobs🦜

Looking for your next role building Agents, RAG apps, or LangGraph integrations? Check the **[LangJobs.dev](https://langjobs.dev/)** board—built for the 150 000-strong AI-Engineering community.  
Post a job or explore openings that use the exact tech stack you're mastering here.

---

## 🤝  Join the Community

- 💬  **Discord** – Private server for Q&A and project feedback  
- 🐙  **GitHub Issues** – Bugs, ideas, PRs welcome!  
- 🛠️  **Bonus Repos** – Extra templates & utilities for course alumni

> All future updates are free. Your one-time enrollment grows with the ecosystem.

Enjoy the course & happy coding! 🎉

---

## 🙏  Acknowledgements

Big thanks to the **LangChain / LangGraph** team and their excellent [documentation and tutorials](https://langchain-ai.github.io/langgraph/tutorials/introduction/) that make this course possible.

---
