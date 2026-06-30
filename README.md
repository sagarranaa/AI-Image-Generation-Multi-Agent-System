# 🎨 AI Image Generation Multi-Agent System

An AI-powered Image Generation system built using **LangGraph**, **LangChain**, and **Groq LLM** with a **Multi-Agent Architecture**.

This project demonstrates how multiple AI agents collaborate to transform a simple user prompt into a high-quality image generation request.

---

# 🚀 Features

- Prompt Enhancement Agent
- Safety Validation Agent
- Style Selection Agent
- Image Generation Agent
- Shared State Management
- Modular LangGraph Architecture
- Easy to replace Image Provider
- Production Ready Folder Structure

---

# 🏗️ Architecture

```
                User Prompt
                     │
                     ▼
             Prompt Agent
      (Enhance User Prompt)
                     │
                     ▼
             Safety Agent
       (Check Prompt Safety)
                     │
                     ▼
              Style Agent
      (Choose Best Art Style)
                     │
                     ▼
             Image Agent
    (Generate Final Image)
                     │
                     ▼
          Generated Image
```

---

# 📂 Project Structure

```
ai-image-agent/

├── app/
│   ├── agents/
│   ├── graph/
│   ├── llm/
│   ├── prompts/
│   ├── services/
│   ├── state/
│   └── utils/
│
├── frontend/
│
├── outputs/
│
├── main.py
├── .env
├── pyproject.toml
└── README.md
```

---

# 🤖 AI Agents

## 📝 Prompt Agent

Improves the user's prompt by adding:

- Details
- Camera angle
- Lighting
- Realism
- High quality keywords

---

## 🛡️ Safety Agent

Checks whether the prompt is safe for image generation.

---

## 🎨 Style Agent

Automatically selects the most suitable artistic style such as:

- Photorealistic
- Fantasy Art
- Anime
- Watercolor
- Oil Painting
- 3D Render

---

## 🖼️ Image Agent

Generates the final image using an Image Generation Provider.

Current implementation uses **Pollinations AI** for learning purposes.

The provider can easily be replaced with:

- OpenAI Images API
- Google Imagen
- Fal AI
- Replicate
- Stability AI
- Hugging Face

by modifying only:

```
app/services/image_service.py
```

---

# 🧠 Tech Stack

- Python
- LangGraph
- LangChain
- Groq LLM
- Pollinations AI
- Pydantic
- Streamlit

---

# 🎯 Learning Objectives

This project demonstrates:

- Multi-Agent Systems
- AI Workflow Orchestration
- Shared State Management
- Prompt Engineering
- Agent Collaboration
- Clean Software Architecture
- Production Ready Project Structure

---

# 📸 Sample Workflow

```
User:
Generate a dragon flying over mountains

        │
        ▼

Prompt Agent
        │
        ▼

Safety Agent
        │
        ▼

Style Agent
        │
        ▼

Image Agent
        │
        ▼

Generated Image
```

---

# 📌 Future Improvements

- Retry Agent
- Quality Evaluation Agent
- Human Approval Agent
- Multiple Image Models
- Image Upscaling
- Image Variations
- Streamlit UI
- Docker Deployment
- AWS Deployment

---

# ⭐ Author

**Sagar Rana**

If you found this project useful, consider giving it a ⭐ on GitHub.
