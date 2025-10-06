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
