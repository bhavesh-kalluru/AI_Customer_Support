# 🤖 AI Customer Support Agent (Generative AI + RAG)

An **AI-powered Customer Support Agent** built with **Python, Streamlit, and OpenAI GPT models** that can handle real-world customer queries.  
This project demonstrates **Retrieval-Augmented Generation (RAG)**, combining **LLMs + knowledge bases** to provide accurate and context-aware responses.  

---

## 🚀 Features
- 🔹 **Generative AI Responses** – powered by OpenAI GPT (`gpt-4o-mini` for fast responses).  
- 🔹 **FAQ Knowledge Base** – retrieves company-specific answers using **FAISS embeddings**.  
- 🔹 **Order Tracking** – fetches order details from a sample database (`orders.json`).  
- 🔹 **Scalable Design** – works for e-commerce, banking, healthcare, and SaaS support.  
- 🔹 **Simple UI** – interactive chatbot built with **Streamlit**.  

---

## 🛠️ Tech Stack
- **Python 3.9+**  
- [Streamlit](https://streamlit.io/) – chatbot UI  
- [OpenAI API](https://platform.openai.com/) – generative responses  
- [FAISS](https://github.com/facebookresearch/faiss) – vector search engine  
- [SentenceTransformers](https://www.sbert.net/) – text embeddings  
- [JSON / TXT files] – mock order + FAQ data  

---

## 📂 Project Structure
ai_customer_support/
│── app.py # Main Streamlit app
│── backend/
│ ├── rag_engine.py # RAG retrieval logic
│ ├── database.py # Loads FAQs + orders
│── data/
│ ├── faqs.txt # Example company FAQs
│ └── orders.json # Sample order DB
│── requirements.txt # Dependencies
│── README.md # Project docs

yaml
Copy code

---

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ai-customer-support.git
   cd ai-customer-support
Install dependencies:
pip install -r requirements.txt
Add your OpenAI API key:

Option A: Set it in terminal
export OPENAI_API_KEY="sk-xxxxxx"

Run the app:
streamlit run app.py
