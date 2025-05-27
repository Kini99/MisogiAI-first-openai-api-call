# MisogiAI-first-openai-api-call
# First OpenAI API Call

This project demonstrates a basic usage of the OpenAI API using Python. It sends a user-provided prompt to OpenAI's GPT model and prints the assistant's response along with token usage.

---

## 📌 What the Script Does

- Takes a user prompt via console input.
- Uses a fixed system prompt to set the assistant's behavior.
- Sends both prompts to OpenAI's `gpt-3.5-turbo` model.
- Prints the assistant’s reply and total tokens used in the response.

---

## 🛠️ Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/first-openai-api-call.git
cd first-openai-api-call
```

### 2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies:
```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file in the root directory and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

### 5. Run the application:
```bash
python app.py
```

