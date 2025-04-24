# Faz as migrações se necessário (opcional, mas recomendado)
python manage.py migrate --noinput

# Coleta arquivos estáticos
python manage.py collectstatic --noinput

# Inicia o Gunicorn
gunicorn todo.wsgi:application --workers 2 --bind 0.0.0.0:8000