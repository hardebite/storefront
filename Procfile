release: python manage.py migrate
web: gunicorn storefront.wsgi
worker: celery -A storefrot worker