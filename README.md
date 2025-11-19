# News Viewer

A minimal web app that retrieves **current headlines** and supports **keyword search** using the NewsAPI.

## Features
- View top headlines (country selectable)
- Search news by keyword
- Simple UI (HTML/CSS/JS)
- Secure backend proxy (Flask)

## Setup
```bash
cd server
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # Add your API key
python app.py
```
Open http://localhost:5000

## API Routes
- `/api/top-headlines?country=us`
- `/api/search?q=ai`

## License
MIT
