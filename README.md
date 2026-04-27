# Iglesia Backend

Django REST Framework API for Iglesia Cristiana La Roca.

## 🚀 Quick Start

### With Docker
```bash
docker-compose up --build -d
```

API available at `http://localhost:8000/api/`
Admin panel at `http://localhost:8000/admin/`

### Local Development
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## 📋 Apps

- **pages** - Static pages (home, about, etc.)
- **sermons** - Sermon content with series
- **events** - Church events and calendar
- **gallery** - Image galleries by category
- **donations** - Donation campaigns and tracking
- **alliances** - Alliance partnerships with projects
- **contact** - Contact forms, site settings, email notifications

## ⚙️ Environment Variables

```env
DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=True
POSTGRES_DB=iglesia_db
POSTGRES_USER=iglesia_user
POSTGRES_PASSWORD=iglesia_password
POSTGRES_HOST=postgres
POSTGRES_PORT=5432
REDIS_HOST=redis
REDIS_PORT=6379
```

## 🗄️ Database

Migrations are run automatically on container startup. To run manually:

```bash
python manage.py migrate
```

## 🔐 Admin

Create superuser:
```bash
python manage.py createsuperuser
```

Access at `http://localhost:8000/admin/`

## 📧 Email & Async Tasks

Uses Celery + Redis for async tasks:
- Email sending from contact form
- Donation notifications

View worker logs:
```bash
docker-compose logs celery
```

## 💾 Cache

SiteSettings (church contact info, social links) is cached in Redis for 1 hour. To clear:

```bash
docker exec iglesia_redis redis-cli FLUSHALL
```

## 🧪 Testing

```bash
python manage.py test
```

## 📚 API Endpoints

All endpoints prefixed with `/api/`:

- `GET /api/pages/` - List pages
- `GET /api/sermons/` - List sermons
- `GET /api/events/` - List events
- `GET /api/gallery/categories/` - Gallery categories
- `POST /api/contact/` - Submit contact form
- `GET /api/donations/campaigns/` - Donation campaigns
- `GET /api/alliances/` - Alliances with impact projects

See individual app URLs for full endpoint list.

## 🎯 Performance Optimizations

- N+1 query fixes using `annotate(Count(...))`
- Prefetch related objects where needed
- Database indexes on frequently filtered fields
- Connection pooling (CONN_MAX_AGE=600)
- Redis cache for SiteSettings
- Gzip compression in Nginx

## 🔄 CI/CD

Push to main/develop triggers GitHub Actions for:
- Tests
- Linting
- Docker image build
