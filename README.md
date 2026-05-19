# 珠合 (ZhuHe)

珠合品牌独立站 — 面向欧洲市场的珍珠首饰电商平台。

## Tech Stack
- **Backend**: Django + DRF
- **Frontend**: Nuxt 3 + TailwindCSS
- **Database**: PostgreSQL
- **Cache/Queue**: Redis
- **Container**: Docker Compose

## Quick Start
```bash
docker compose up -d
cd backend && pip install -r requirements.txt && python manage.py runserver
cd frontend && npm install && npm run dev
```

## Branch Strategy
- `main` — production
- `develop` — development
- `feature/*` — feature branches
- `fix/*` — fix branches
