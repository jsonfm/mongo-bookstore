### 📚 Bookstore
A simple app made with mongodb and python. It implements simple crud operations across the different data models related to books, authors, reviews, etc.

### ✨ Technologies

- FastAPI
- Mongo


### ⚙️ Setup
1. Create and activate a virtual environment:

```
python -m venv venv
```
2. Install dependencies:
```
pip install -r requirements.txt
```

3. Write the environment variables following `.env.example`:
```
MONGO_URI=""
MONGO_INITDB_ROOT_USERNAME=""
MONGO_INITDB_ROOT_PASSWORD=""
``` 

### ⚡️ Development

```bash
uvicorn main:app --port 8000 --reload
```

### 🐋 MongoDB
```
docker compose up -d
```