    # 🤖 GenAI Projects — Learning Journey

    A structured, day-by-day log of my journey from Python beginner to GenAI/LLM Engineer.  
    Every folder contains working code written and tested that day — no copy-paste, built from scratch.

    ---

    ## 🗺️ Roadmap

    | Phase | Focus | Status |
    |-------|-------|--------|
    | Week 1 (Days 1–5) | Python for AI | ✅ Complete |
    | Mini Project 1 | Local Text Summarizer | ✅ Complete |
    | Week 2 (Days 8–12) | APIs + OpenAI + Streamlit | 🔄 In Progress |
    | Week 3+ | LangChain + RAG Pipeline | 🔜 Coming Soon |

    ---

    ## 📁 Folder Structure

    ```
    genai-projects/
    ├── day1/
    ├── day2/
    ├── day3/
    ├── day4/
    ├── day5/
    ├── miniProject1-text-summarizer/
    └── README.md
    ```

    ---

    ## 📅 Day-by-Day Progress

    ### Day 1 — Functions, Loops & List Comprehensions
    **Folder:** `day1/`  
    **Concepts:** `def`, `return`, `for` loops, list comprehensions, filtering

    **What I built:**
    - `word_count(sentence)` — counts words in a sentence
    - `filter_arr(sentences, minLength)` — filters sentences by minimum word count
    - `filter_sentences(sentences, minLength)` — filters AND converts to uppercase in one list comprehension

    **Key learning:**  
    The `filter_sentences()` function is the same logic used in RAG pipelines to filter irrelevant text chunks before embedding.

    ---

    ### Day 2 — Dictionaries & JSON
    **Folder:** `day2/`  
    **Concepts:** `dict`, `.get()`, nested dictionaries, `json.loads()`, `json.dumps()`

    **What I built:**
    - Created and accessed nested dictionaries mimicking real OpenAI API responses
    - `summarise_responses(responses)` — parses a list of JSON strings and extracts answer + token count from each

    **Key learning:**  
    Every LLM API response is JSON. Practiced extracting `choices[0]["message"]["content"]` — the exact path used to read OpenAI responses in real projects.

    ---

    ### Day 3 — File I/O & Text Chunking
    **Folder:** `day3/`  
    **Concepts:** `open()`, `read()`, `readlines()`, `write()`, `with` statement, `.strip()`, `.split()`

    **What I built:**
    - Read a `.txt` file and counted total words
    - Filtered lines containing specific keywords
    - `chunk_and_save(filepath, chunk_size)` — splits a document into N-word chunks and saves to a new file

    **Key learning:**  
    Text chunking is step 1 of every RAG pipeline. The chunker built today is the same logic used before sending documents to an embedding model.

    ---

    ### Day 4 — Classes & OOP
    **Folder:** `day4/`  
    **Concepts:** `class`, `__init__`, `self`, methods, storing lists inside objects

    **What I built:**
    - `AIModel` — stores model name and max tokens, has a `describe()` method
    - `TokenTracker` — tracks total tokens used across API calls with `add()`, `get_total()`, `reset()`
    - `ChatHistory` — stores conversation as a list of role/content dicts with `add()`, `get_all()`, `last(n)`, `clear()`, `count()`

    **Key learning:**  
    `ChatHistory` is exactly what LangChain's `ConversationBufferMemory` does internally. Built the memory system of a chatbot from scratch.

    ---

    ### Day 5 — Environment Variables & Error Handling
    **Folder:** `day5/`  
    **Concepts:** `.env` files, `python-dotenv`, `os.getenv()`, `try/except`, `raise ValueError`

    **What I built:**
    - Loaded API keys safely from a `.env` file using `python-dotenv`
    - `safe_divide(a, b)` — handles ZeroDivisionError gracefully
    - `load_config()` — production-ready config loader that raises clear errors for missing keys and handles invalid values with safe defaults

    **Key learning:**  
    API keys must never be hardcoded. `load_config()` is the exact pattern used at the top of every real GenAI project.

    ---

    ## 🏗️ Mini Project 1 — Local Text Summarizer
    **Folder:** `miniProject1-text-summarizer/`

    ### What it does
    Reads a `.txt` document, splits it into chunks, extracts a summary from each chunk, and saves the results to an output file — all with safe config loading and error handling.

    ### How to run
    ```bash
    # 1. Install dependencies
    pip install python-dotenv

    # 2. Create a .env file
    echo "OPENAI_API_KEY=your-key-here" > .env
    echo "MODEL_NAME=gpt-4o-mini" >> .env
    echo "MAX_TOKENS=1000" >> .env

    # 3. Run
    python summarizer.py
    ```

    ### Output
    ```
    Using model: gpt-4o-mini

    Total chunks: 5

    Chunk 1 done ✓
    Chunk 2 done ✓
    Chunk 3 done ✓
    Chunk 4 done ✓
    Chunk 5 done ✓

    Done! Saved 5 summaries to summary_output.txt
    ```

    ### Functions built
    | Function | What it does |
    |----------|-------------|
    | `load_config()` | Loads and validates .env variables |
    | `chunk_text(filepath, chunk_size)` | Splits document into N-word chunks |
    | `summarize_chunk(chunk)` | Extracts first sentence as summary |
    | `main()` | Ties everything together, saves output |

    ### Week 2 upgrade
    `summarize_chunk()` will be replaced with a real OpenAI API call — everything else stays identical. The skeleton is already production-ready.

    ---

    ## 🛠️ Tech Stack

    ![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
    ![OpenAI](https://img.shields.io/badge/OpenAI-API-green?logo=openai)
    ![LangChain](https://img.shields.io/badge/LangChain-coming_soon-orange)
    ![Streamlit](https://img.shields.io/badge/Streamlit-coming_soon-red)

    ---

    ## 📈 What's coming next

    - **Day 8–9** — Calling real APIs + first OpenAI API call
    - **Day 10** — Terminal chatbot with conversation memory
    - **Day 11** — Streamlit UI + live deployment
    - **Day 12** — Prompt engineering
    - **Mini Project 2** — AI-powered app deployed live (Streamlit Cloud)
    - **Week 3** — LangChain + RAG PDF chatbot

    ---

    ## 👤 About

    Self-taught GenAI engineer in training, based in Hyderabad 🇮🇳  
    Building in public — one day at a time.

Connect with me on [LinkedIn](https://www.linkedin.com/in/mohammed-mubashir-ali-hyd658)
