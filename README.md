# AI baba

AI baba is a Streamlit-based Generative AI mini project that combines:

- Zodiac sign detection from date of birth
- PDF-based knowledge ingestion from internet sources
- RAG using chunking + embeddings + FAISS vector store
- Gemini text generation for concise zodiac readings
- Puter.js frontend image generation for incident scene visualization

## Features

- Takes user name and DOB
- Detects zodiac sign
- Downloads zodiac-related PDFs from the internet
- Builds a FAISS vector database from extracted PDF text
- Retrieves relevant zodiac context using RAG
- Sends retrieved context to Gemini for grounded output
- Produces:
  - zodiac sign
  - personality snapshot
  - lucky color
  - lucky number
  - best hour
  - daily incident prediction
  - image prompt
- Uses Puter.js in frontend JavaScript to generate an image without backend image API code

## Setup

### 1. Create virtual environment
```bash
python -m venv venv
```

### 2. Activate it
#### Windows
```bash
venv\Scripts\activate
```

#### macOS/Linux
```bash
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Create `.env`
```env
GEMINI_API_KEY=your_key_here
```

### 5. Run
```bash
streamlit run app.py
```

## Notes

- Gemini API requires your API key.
- Puter.js image generation runs in the browser and may ask the user to authenticate with Puter.
- First run may take time because PDFs are downloaded and indexed.