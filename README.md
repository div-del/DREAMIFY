# ✨ Dreamify 🎬

> **Turn your dreams into animated GIFs using AI!**  
> Dreamify is a powerful Text-to-GIF application that generates "dreamy" animated scenes from simple text prompts.

![Dreamify Banner](https://img.shields.io/badge/Status-Active-success)
![Python](https://img.shields.io/badge/Backend-FastAPI-blue?logo=fastapi)
![React](https://img.shields.io/badge/Frontend-React_Vite-61DAFB?logo=react)
![Tailwind](https://img.shields.io/badge/Style-TailwindCSS-38B2AC?logo=tailwindcss)

---

## 🚀 About The Project

Dreamify uses advanced AI models (like **FLUX.1-schnell** & **Stable Diffusion**) via the Hugging Face Inference API to generate sequential frames based on your text input. It then intelligently stitches these frames together into a smooth, animated GIF, perfect for sharing.

### ✨ Features
- **📝 Text-to-GIF**: Just type a prompt, and watch it come to life.
- **🎥 Multi-Frame Generation**: Automatically generates 5 distinct frames (beginning, motion, conclusion) for a coherent mini-story.
- **🎨 Dreamy UI**: A beautiful, immersive "Dark/Rainforest" themed interface with neon accents.
- **⚡ Fast & Efficient**: Powered by Vite and FastAPI for lightning-fast performance.
- **🛠️ Smart Fallback**: Automatically switches between multiple high-performance AI models if one is busy.

---

## 🛠️ Tech Stack

### Backend
- **Framework**: [FastAPI](https://fastapi.tiangolo.com/) (Python)
- **Image Processing**: [Pillow](https://python-pillow.org/) (GIF stitching)
- **AI Integration**: Hugging Face Inference API
- **Models**: FLUX.1-schnell, Stable Diffusion 3.5 Large

### Frontend
- **Framework**: [React](https://reactjs.org/) + [Vite](https://vitejs.dev/)
- **Styling**: [TailwindCSS](https://tailwindcss.com/)
- **State Management**: React Hooks
- **HTTP Client**: Axios

---

## 🏁 Getting Started

Follow these steps to get a local copy up and running.

### Prerequisites
- Python 3.8+
- Node.js & npm

### 📥 1. Clone the Repository
```bash
git clone https://github.com/your-username/dreamify.git
cd dreamify
```

### ⚙️ 2. Backend Setup
Navigate to the backend folder and set up the Python environment.

```bash
# Navigate to the project root
# Create virtual environment (optional but recommended)
python -m venv .venv

# Activate virtual environment
# Windows:
.\.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r backend/requirements.txt
```

**🔑 Environment Configuration:**
Create a `.env` file in the `backend/` directory:
```env
HF_TOKEN=your_hugging_face_write_token_here
```
*(You can get a free token from [Hugging Face Settings](https://huggingface.co/settings/tokens))*

### 🎨 3. Frontend Setup
Open a new terminal configuration for the frontend.

```bash
cd frontend
npm install
```

---

## 🏃 Run the Application

You need to run both the backend and frontend terminals simultaneously.

### Terminal 1: Backend
```bash
# Make sure your venv is activated
python backend/main.py
```
*Backend will run on `http://127.0.0.1:8000`*

### Terminal 2: Frontend
```bash
cd frontend
npm run dev
```
*Frontend will run on `http://localhost:5173`*

---

## 🎮 Usage

1. Open `http://localhost:5173` in your browser.
2. Enter a creative prompt (e.g., *"A cyberpunk city in the rain, neon lights reflecting on wet pavement"*).
3. Click **Generate**.
4. Wait a few seconds while the AI dreams up your GIF.
5. Hover over the result to see the animation!

---

## 🤝 Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

<p align="center">Made with ❤️ and ☕ by Nameeta 🤗</p>
