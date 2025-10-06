# Open Library - Monorepo
open-library/
├─ .github/
│  ├─ PULL_REQUEST_TEMPLATE.md
│  └─ workflows/ci.yml
├─ infra/
│  └─ docker-compose.yml
├─ backend/
│  ├─ Dockerfile
│  ├─ requirements.txt
│  └─ app/
│     ├─ main.py
│     ├─ config.py
│     ├─ db.py
│     ├─ models.py
│     ├─ schemas.py
│     ├─ routers/
│     │  ├─ auth.py
│     │  ├─ files.py
│     │  └─ chat.py
│     └─ services/
│        ├─ storage.py
│        └─ background.py
├─ frontend/
│  ├─ package.json
│  └─ src/
│     ├─ App.jsx
│     ├─ pages/
│     └─ components/
├─ docs/
│  └─ roadmap.md
├─ .gitignore
└─ README.md


#  Open Digital Library - MVP

##  Project Goal
MVP’s purpose is to deliver the **core functionality** of the platform:
- User **registration & login**
- Ability to **upload PDF files**
- A **public library** where uploaded PDFs are listed and downloadable
- Basic **chat room creation** and messaging

This MVP is the foundation for the larger vision: a modern **Open Digital Library (Digital Alexandria)**.
