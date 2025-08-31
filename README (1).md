# 🕸️ AI Web Scraper

AI Web Scraper is an intelligent web scraping application that extracts website content and uses **LLMs** to parse and analyze the scraped data.  
It is built with **Streamlit**, **Selenium**, **BeautifulSoup**, and **LangChain with Ollama** for natural language parsing.

---

## 🚀 Features
- 🌐 **Scrape Any Website** – Extracts page content using Selenium + BeautifulSoup.  
- 🧹 **Cleaned DOM Content** – Removes unnecessary scripts, styles, and formats the text.  
- ✂️ **Chunking** – Splits large DOM content into manageable chunks for processing.  
- 🤖 **AI-Powered Parsing** – Uses **LangChain + Ollama LLM** to parse and extract information based on user queries.  
- 📊 **Interactive UI** – Streamlit-based web interface for scraping and querying data.  

---

## 🛠️ Tech Stack
- [Python](https://www.python.org/)  
- [Streamlit](https://streamlit.io/) – Web UI  
- [Selenium](https://www.selenium.dev/) – Automated web scraping  
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) – HTML parsing  
- [LangChain](https://www.langchain.com/) – Orchestration framework  
- [Ollama](https://ollama.com/) – LLM for natural language processing  

---

## 📂 Project Structure
```
AI-Web-Scraper/
│── main.py              # Streamlit UI entry point
│── scrape.py            # Scraping utilities (Selenium + BeautifulSoup)
│── parse.py             # Parsing logic with LangChain + Ollama
│── requirements.txt     # Project dependencies
│── chromedriver.exe     # Chrome WebDriver (for Selenium)
```

---

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/ai-web-scraper.git
   cd ai-web-scraper
   ```

2. **Set up a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate      # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set environment variables** (optional)
   - Create a `.env` file to configure custom settings like `TARGET_URL`.

---

## ▶️ Usage

Run the Streamlit app:
```bash
streamlit run main.py
```

- Enter a **website URL** in the text box.  
- Scrape and view the **cleaned DOM content**.  
- Describe what you want to extract (e.g., "List all product names and prices").  
- Let the AI parse the results using **Ollama LLM**.  

---

## 📝 Example Workflow
1. Input: `https://example.com/products`  
2. Query: `"Extract all product names and their prices"`  
3. Output: AI returns a structured list of products with corresponding prices.  

---

## 🔮 Future Improvements
- [ ] Add database storage (SQLite / MongoDB)  
- [ ] Enable export to CSV/Excel  
- [ ] Add support for multiple LLM providers  
- [ ] Enhance CAPTCHA handling  

---

## 📜 License
This project is licensed under the **MIT License**. Feel free to use and modify it.
